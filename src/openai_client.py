#!/usr/bin/env python3
"""
OpenAI API Client
A simple client for interacting with OpenAI's API
"""

import os
import sys
from typing import List, Optional
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

class OpenAIClient:
    """A wrapper class for OpenAI API interactions."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the OpenAI client.
        
        Args:
            api_key: Optional API key. If not provided, will use OPENAI_API_KEY from environment.
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY environment variable.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.default_model = os.getenv('DEFAULT_MODEL', 'gpt-3.5-turbo')
        self.max_tokens = int(os.getenv('MAX_TOKENS', 1500))
        self.temperature = float(os.getenv('TEMPERATURE', 0.7))
    
    def chat_completion(self, 
                       messages: List[dict], 
                       model: Optional[str] = None,
                       max_tokens: Optional[int] = None,
                       temperature: Optional[float] = None) -> str:
        """
        Generate a chat completion using OpenAI's API.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            model: Model to use (defaults to configured default)
            max_tokens: Maximum tokens in response
            temperature: Temperature for randomness (0.0 to 1.0)
            
        Returns:
            The generated response text
        """
        try:
            response = self.client.chat.completions.create(
                model=model or self.default_model,
                messages=messages,
                max_tokens=max_tokens or self.max_tokens,
                temperature=temperature or self.temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    
    def simple_completion(self, prompt: str, **kwargs) -> str:
        """
        Generate a simple completion from a prompt.
        
        Args:
            prompt: The input prompt
            **kwargs: Additional parameters for chat_completion
            
        Returns:
            The generated response text
        """
        messages = [{"role": "user", "content": prompt}]
        return self.chat_completion(messages, **kwargs)
    
    def conversation(self, system_prompt: str, user_message: str, **kwargs) -> str:
        """
        Generate a response with a system prompt and user message.
        
        Args:
            system_prompt: System message to set context/behavior
            user_message: User's message
            **kwargs: Additional parameters for chat_completion
            
        Returns:
            The generated response text
        """
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
        return self.chat_completion(messages, **kwargs)

def main():
    """Example usage of the OpenAI client."""
    try:
        client = OpenAIClient()
        
        print("OpenAI API Client Test")
        print("=" * 50)
        
        # Simple completion example
        print("\n1. Simple Completion:")
        response = client.simple_completion("Explain what artificial intelligence is in one paragraph.")
        print(f"Response: {response}")
        
        # Conversation with system prompt example
        print("\n2. Conversation with System Prompt:")
        system_prompt = "You are a helpful Python programming assistant."
        user_message = "How do I read a CSV file in Python?"
        response = client.conversation(system_prompt, user_message)
        print(f"Response: {response}")
        
        # Multi-turn conversation example
        print("\n3. Multi-turn Conversation:")
        messages = [
            {"role": "system", "content": "You are a creative writing assistant."},
            {"role": "user", "content": "Write the first sentence of a mystery novel."},
            {"role": "assistant", "content": "The old lighthouse keeper hadn't been seen for three days, but his light still swept across the harbor every night at exactly midnight."},
            {"role": "user", "content": "Continue the story with the next sentence."}
        ]
        response = client.chat_completion(messages)
        print(f"Response: {response}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()