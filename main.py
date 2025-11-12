"""
Main demonstration script for AI in Software Engineering
"""

import os
import sys

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from ai_code_generator import AICodeGenerator
from ai_test_automation import AITestAutomation
from code_analyzer import AICodeAnalyzer

def demonstrate_ai_code_generation():
    """Demonstrate AI-powered code generation"""
    print("🚀 AI CODE GENERATION DEMONSTRATION")
    print("=" * 50)
    
    generator = AICodeGenerator()
    
    # Generate various functions
    functions_to_generate = [
        "sorts a list of dictionaries by a specific key",
        "reads a CSV file and returns the data as a list of dictionaries",
        "validates an email address format",
        "sends an HTTP GET request and handles errors"
    ]
    
    for desc in functions_to_generate:
        print(f"\nGenerating function: {desc}")
        code = generator.generate_function(desc)
        print(code)
        print("-" * 30)

def demonstrate_ai_testing():
    """Demonstrate AI-enhanced testing"""
    print("\n🎯 AI TEST AUTOMATION DEMONSTRATION")
    print("=" * 50)
    
    tester = AITestAutomation()
    
    # Show test data generation
    print("Generated Test Data:")
    print(f"Emails: {tester.generate_test_data('emails', 3)}")
    print(f"Usernames: {tester.generate_test_data('usernames', 2)}")
    
    # Demonstrate element finding strategies
    print("\nElement Location Strategies:")
    strategies = [
        "By text content",
        "By placeholder",
        "By label",
        "By common attributes"
    ]
    for strategy in strategies:
        print(f"  - {strategy}")

def demonstrate_code_analysis():
    """Demonstrate AI-powered code analysis"""
    print("\n🔍 AI CODE ANALYSIS DEMONSTRATION")
    print("=" * 50)
    
    analyzer = AICodeAnalyzer()
    
    sample_code = '''
def complex_function(data):
    """A function with some complexity for analysis."""
    result = []
    for item in data:
        if item > 100:
            if item < 200:
                if item % 2 == 0:
                    result.append(item * 2)
                else:
                    result.append(item * 3)
            else:
                result.append(item)
        else:
            result.append(0)
    
    x = 1000  # Magic number
    return result
'''
    
    report = analyzer.generate_analysis_report(sample_code)
    print(report)

def main():
    """Main demonstration function"""
    print("🤖 AI IN SOFTWARE ENGINEERING - COMPLETE DEMONSTRATION")
    print("=" * 60)
    
    demonstrate_ai_code_generation()
    demonstrate_ai_testing()
    demonstrate_code_analysis()
    
    print("\n" + "=" * 60)
    print("✅ DEMONSTRATION COMPLETE")
    print("\nKey Benefits Demonstrated:")
    print("  • Automated code generation")
    print("  • Intelligent test automation")
    print("  • Comprehensive code analysis")
    print("  • Quality and security insights")
    print("  • Enhanced developer productivity")

if __name__ == "__main__":
    main()
