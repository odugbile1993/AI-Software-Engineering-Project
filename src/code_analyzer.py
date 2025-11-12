"""
AI-Powered Code Analysis Module
Analyzes code quality and provides insights
"""

import ast
import re
from typing import List, Dict, Any

class AICodeAnalyzer:
    def __init__(self):
        self.complexity_threshold = 10
        self.max_function_length = 50
    
    def analyze_code_complexity(self, code: str) -> Dict[str, Any]:
        """Analyze code complexity using various metrics"""
        
        analysis_result = {
            'cyclomatic_complexity': 0,
            'lines_of_code': 0,
            'function_count': 0,
            'issue_count': 0,
            'issues': [],
            'maintainability_index': 0,
            'security_concerns': []
        }
        
        try:
            # Parse the code into AST
            tree = ast.parse(code)
            
            # Calculate basic metrics
            analysis_result['lines_of_code'] = len(code.split('\n'))
            analysis_result['function_count'] = len([
                node for node in ast.walk(tree) 
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            ])
            
            # Calculate cyclomatic complexity
            analysis_result['cyclomatic_complexity'] = self._calculate_cyclomatic_complexity(tree)
            
            # Find potential issues
            analysis_result['issues'] = self._find_code_issues(tree, code)
            analysis_result['issue_count'] = len(analysis_result['issues'])
            
            # Calculate maintainability index (simplified)
            analysis_result['maintainability_index'] = self._calculate_maintainability_index(
                analysis_result['cyclomatic_complexity'],
                analysis_result['lines_of_code'],
                analysis_result['issue_count']
            )
            
            # Check for security concerns
            analysis_result['security_concerns'] = self._find_security_concerns(code)
            
        except SyntaxError as e:
            analysis_result['issues'].append(f"Syntax error: {e}")
            analysis_result['issue_count'] += 1
        
        return analysis_result
    
    def _calculate_cyclomatic_complexity(self, tree: ast.AST) -> int:
        """Calculate cyclomatic complexity from AST"""
        complexity = 1  # Base complexity
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.AsyncFor)):
                complexity += 1
            elif isinstance(node, (ast.And, ast.Or)):
                complexity += 1
            elif isinstance(node, ast.Try):
                complexity += len(node.handlers)
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1
        
        return complexity
    
    def _find_code_issues(self, tree: ast.AST, code: str) -> List[str]:
        """Find potential code issues and anti-patterns"""
        issues = []
        
        # Check for long functions
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                function_lines = node.end_lineno - node.lineno if node.end_lineno else 0
                if function_lines > self.max_function_length:
                    issues.append(f"Function '{node.name}' is too long ({function_lines} lines)")
        
        # Check for missing docstrings
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Module)):
                if not ast.get_docstring(node):
                    if isinstance(node, ast.FunctionDef):
                        issues.append(f"Function '{node.name}' is missing a docstring")
                    elif isinstance(node, ast.ClassDef):
                        issues.append(f"Class '{node.name}' is missing a docstring")
                    elif isinstance(node, ast.Module):
                        issues.append("Module is missing a docstring")
        
        # Check for broad except clauses
        for node in ast.walk(tree):
            if isinstance(node, ast.ExceptHandler):
                if node.type is None:
                    issues.append("Bare except clause found - specify exception types")
        
        # Check for potential code smells using regex patterns
        patterns = {
            'magic_numbers': r'\b\d{3,}\b',
            'long_lines': r'.{100,}',
        }
        
        for line_num, line in enumerate(code.split('\n'), 1):
            if re.search(patterns['magic_numbers'], line) and not re.search(r'#', line):
                issues.append(f"Potential magic number in line {line_num}")
            if re.search(patterns['long_lines'], line):
                issues.append(f"Line {line_num} is too long")
        
        return issues
    
    def _find_security_concerns(self, code: str) -> List[str]:
        """Identify potential security issues"""
        security_issues = []
        
        # Pattern-based security checks
        security_patterns = {
            'eval_usage': r'eval\s*\(',
            'exec_usage': r'exec\s*\(',
            'shell_true': r'shell=True',
            'sql_string_concat': r'SELECT.*\+',
            'hardcoded_passwords': r'password\s*=\s*[\'\"][^\'\"]+[\'\"]',
        }
        
        for issue_type, pattern in security_patterns.items():
            if re.search(pattern, code, re.IGNORECASE):
                security_issues.append(f"Potential security concern: {issue_type.replace('_', ' ')}")
        
        return security_issues
    
    def _calculate_maintainability_index(self, complexity: int, loc: int, issues: int) -> float:
        """Calculate simplified maintainability index"""
        # Simplified calculation for demonstration
        base_score = 100
        complexity_penalty = complexity * 2
        loc_penalty = min(loc / 10, 20)
        issues_penalty = issues * 5
        
        maintainability = base_score - complexity_penalty - loc_penalty - issues_penalty
        return max(0, min(100, maintainability))
    
    def generate_analysis_report(self, code: str) -> str:
        """Generate a comprehensive code analysis report"""
        analysis = self.analyze_code_complexity(code)
        
        report = []
        report.append("CODE ANALYSIS REPORT")
        report.append("=" * 50)
        report.append(f"Lines of Code: {analysis['lines_of_code']}")
        report.append(f"Function Count: {analysis['function_count']}")
        report.append(f"Cyclomatic Complexity: {analysis['cyclomatic_complexity']}")
        report.append(f"Maintainability Index: {analysis['maintainability_index']:.1f}/100")
        report.append(f"Issues Found: {analysis['issue_count']}")
        
        if analysis['issues']:
            report.append("\nISSUES:")
            for issue in analysis['issues']:
                report.append(f"  - {issue}")
        
        if analysis['security_concerns']:
            report.append("\nSECURITY CONCERNS:")
            for concern in analysis['security_concerns']:
                report.append(f"  ⚠️  {concern}")
        
        # Overall assessment
        if analysis['maintainability_index'] > 80:
            assessment = "EXCELLENT - Code is highly maintainable"
        elif analysis['maintainability_index'] > 60:
            assessment = "GOOD - Code is maintainable with minor improvements needed"
        elif analysis['maintainability_index'] > 40:
            assessment = "FAIR - Code requires significant refactoring"
        else:
            assessment = "POOR - Major refactoring required"
        
        report.append(f"\nOVERALL ASSESSMENT: {assessment}")
        
        return '\n'.join(report)

# Example usage and demonstration
if __name__ == "__main__":
    analyzer = AICodeAnalyzer()
    
    # Sample code to analyze
    sample_code = '''
def calculate_stats(numbers):
    """Calculate basic statistics from a list of numbers."""
    if not numbers:
        return None
    
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    
    average = total / count if count > 0 else 0
    
    # This is a very long line that should trigger the long line detection in the code analysis because it exceeds the typical maximum line length guidelines
    max_value = max(numbers) if numbers else 0
    min_value = min(numbers) if numbers else 0
    
    return {
        "average": average,
        "max": max_value,
        "min": min_value,
        "count": count,
        "total": total
    }

def risky_function(data):
    try:
        result = eval(data)  # This is a security risk
        return result
    except:
        return None
'''
    
    print("AI CODE ANALYSIS DEMO")
    print("=" * 50)
    
    report = analyzer.generate_analysis_report(sample_code)
    print(report)
