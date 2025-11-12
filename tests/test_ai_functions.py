"""
Test cases for AI-powered functions
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from ai_code_generator import AICodeGenerator
from code_analyzer import AICodeAnalyzer

class TestAICodeGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = AICodeGenerator()
    
    def test_mock_function_generation(self):
        """Test that mock function generation works without API key"""
        code = self.generator.generate_function("sorts a list of dictionaries by a specific key")
        self.assertIsNotNone(code)
        self.assertIn("def sort_list_of_dicts", code)
    
    def test_code_review_mock(self):
        """Test mock code review functionality"""
        sample_code = "def test():\n    return 42"
        review = self.generator.code_review(sample_code)
        self.assertIsNotNone(review)

class TestAICodeAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = AICodeAnalyzer()
    
    def test_analyze_simple_code(self):
        """Test analysis of simple Python code"""
        simple_code = """
def hello_world():
    return "Hello, World!"
"""
        analysis = self.analyzer.analyze_code_complexity(simple_code)
        self.assertEqual(analysis['function_count'], 1)
        self.assertGreaterEqual(analysis['maintainability_index'], 0)
    
    def test_issue_detection(self):
        """Test that code issues are properly detected"""
        problematic_code = """
def bad_function():
    x = 1000  # Magic number
    if True:
        if False:
            if 1 == 1:
                return "Deeply nested"
"""
        analysis = self.analyzer.analyze_code_complexity(problematic_code)
        self.assertGreater(analysis['issue_count'], 0)

if __name__ == '__main__':
    unittest.main()
