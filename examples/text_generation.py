#!/usr/bin/env python3
"""
Text Generation Examples
Demonstrates various text generation capabilities using OpenAI API
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from openai_client import OpenAIClient

def creative_writing_example():
    """Example of creative writing with OpenAI."""
    client = OpenAIClient()
    
    print("Creative Writing Example")
    print("-" * 30)
    
    # Story generation
    prompt = """Write a short story (3-4 paragraphs) about a robot who discovers emotions for the first time. 
    The story should be touching and explore themes of consciousness and humanity."""
    
    response = client.simple_completion(prompt, temperature=0.8, max_tokens=500)
    print("Generated Story:")
    print(response)

def text_summarization_example():
    """Example of text summarization."""
    client = OpenAIClient()
    
    print("\n\nText Summarization Example")
    print("-" * 35)
    
    long_text = """
    Artificial Intelligence (AI) is a branch of computer science that aims to create intelligent machines 
    that can think and learn like humans. The field of AI research was founded at a conference at Dartmouth 
    College in 1956, where the term "artificial intelligence" was coined. AI encompasses various subfields 
    including machine learning, natural language processing, computer vision, and robotics. Machine learning, 
    a subset of AI, focuses on the development of algorithms that can learn from and make decisions based on data. 
    Deep learning, which is a subset of machine learning, uses neural networks with multiple layers to model 
    and understand complex patterns in data. AI has found applications in numerous industries including healthcare, 
    finance, transportation, and entertainment. Some notable AI achievements include defeating world champions 
    in chess and Go, enabling self-driving cars, and powering virtual assistants like Siri and Alexa. However, 
    AI also presents challenges including ethical concerns about bias and fairness, privacy issues, and questions 
    about the future impact on employment. As AI continues to advance, it's important to develop it responsibly 
    and consider its societal implications.
    """
    
    system_prompt = "You are a helpful assistant that creates concise summaries."
    user_message = f"Please summarize the following text in 2-3 sentences:\n\n{long_text}"
    
    response = client.conversation(system_prompt, user_message)
    print("Original text length:", len(long_text.split()))
    print("\nSummary:")
    print(response)

def language_translation_example():
    """Example of language translation."""
    client = OpenAIClient()
    
    print("\n\nLanguage Translation Example")
    print("-" * 35)
    
    english_text = "Hello, how are you today? I hope you're having a wonderful day!"
    
    # Translate to different languages
    languages = ["Spanish", "French", "German", "Japanese"]
    
    for language in languages:
        prompt = f"Translate the following English text to {language}: '{english_text}'"
        response = client.simple_completion(prompt, temperature=0.3)
        print(f"{language}: {response}")

def code_generation_example():
    """Example of code generation."""
    client = OpenAIClient()
    
    print("\n\nCode Generation Example")
    print("-" * 30)
    
    system_prompt = "You are a helpful programming assistant that writes clean, well-commented code."
    user_message = """Write a Python function that takes a list of numbers and returns:
    1. The sum of all numbers
    2. The average
    3. The maximum and minimum values
    
    The function should handle edge cases like empty lists."""
    
    response = client.conversation(system_prompt, user_message, temperature=0.2)
    print("Generated Code:")
    print(response)

def main():
    """Run all text generation examples."""
    try:
        creative_writing_example()
        text_summarization_example()
        language_translation_example()
        code_generation_example()
        
    except Exception as e:
        print(f"Error running examples: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()