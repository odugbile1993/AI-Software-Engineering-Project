"""
AI-Powered Code Generation Module
Automates repetitive coding tasks using OpenAI API
"""

import openai
import os
from dotenv import load_dotenv

load_dotenv()

class AICodeGenerator:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if self.api_key:
            self.client = openai.OpenAI(api_key=self.api_key)
        else:
            self.client = None
            print("Warning: OPENAI_API_KEY not found. Using mock mode.")
    
    def generate_function(self, description, language="python"):
        """Generate code based on natural language description"""
        
        # Mock response for demonstration (remove when using real API)
        if not self.client:
            return self._mock_generate_function(description, language)
        
        prompt = f"""
        Write a {language} function that: {description}
        
        Requirements:
        - Include proper error handling
        - Add comprehensive docstring
        - Use type hints
        - Follow best practices
        - Return appropriate values
        
        Provide only the code without explanations.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert software engineer."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"Error generating code: {str(e)}"
    
    def _mock_generate_function(self, description, language):
        """Mock function for demonstration without API key"""
        mock_functions = {
            "python": {
                "sorts a list of dictionaries by a specific key": '''
def sort_list_of_dicts(data, key):
    """
    Sorts a list of dictionaries by a specified key.
    
    Args:
        data (list): List of dictionaries to sort
        key (str): Key to sort by
    
    Returns:
        list: Sorted list of dictionaries
    
    Raises:
        ValueError: If key is not present in dictionaries
    """
    if not data:
        return []
    
    if key not in data[0]:
        raise ValueError(f"Key '{key}' not found in dictionaries")
    
    return sorted(data, key=lambda x: x[key])
''',
                "reads a CSV file and returns the data as a list of dictionaries": '''
import csv
from typing import List, Dict

def read_csv_file(file_path: str) -> List[Dict]:
    """
    Reads a CSV file and converts it to a list of dictionaries.
    
    Args:
        file_path (str): Path to the CSV file
    
    Returns:
        List[Dict]: List of dictionaries representing rows
    
    Raises:
        FileNotFoundError: If file doesn't exist
        Exception: For other file reading errors
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            return list(csv_reader)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")
'''
            }
        }
        
        return mock_functions.get(language, {}).get(description, "# Code generation not available in mock mode")

    def code_review(self, code_snippet):
        """Perform AI-powered code review"""
        if not self.client:
            return "Mock code review: Code appears functional but needs proper error handling."
        
        prompt = f"""
        Review this code and provide constructive feedback:
        
        {code_snippet}
        
        Focus on:
        - Code quality and readability
        - Potential bugs or issues
        - Security concerns
        - Performance improvements
        - Best practices adherence
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an experienced code reviewer."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error in code review: {str(e)}"

# Example usage and demonstration
if __name__ == "__main__":
    generator = AICodeGenerator()
    
    # Generate a sorting function
    sorting_code = generator.generate_function("sorts a list of dictionaries by a specific key")
    print("Generated Sorting Function:")
    print(sorting_code)
    print("\n" + "="*50 + "\n")
    
    # Generate CSV reader function
    csv_code = generator.generate_function("reads a CSV file and returns the data as a list of dictionaries")
    print("Generated CSV Reader Function:")
    print(csv_code)
