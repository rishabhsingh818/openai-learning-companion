#!/usr/bin/env python3
"""
Chatbot Example
Demonstrates how to create an interactive chatbot using OpenAI API
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from openai_client import OpenAIClient

class ChatBot:
    """A simple chatbot using OpenAI API."""
    
    def __init__(self, system_prompt: str = None):
        """
        Initialize the chatbot.
        
        Args:
            system_prompt: Optional system prompt to set the chatbot's personality
        """
        self.client = OpenAIClient()
        self.conversation_history = []
        
        if system_prompt:
            self.conversation_history.append({"role": "system", "content": system_prompt})
    
    def chat(self, user_input: str) -> str:
        """
        Send a message to the chatbot and get a response.
        
        Args:
            user_input: The user's message
            
        Returns:
            The chatbot's response
        """
        # Add user message to history
        self.conversation_history.append({"role": "user", "content": user_input})
        
        # Get response from OpenAI
        response = self.client.chat_completion(self.conversation_history)
        
        # Add assistant response to history
        self.conversation_history.append({"role": "assistant", "content": response})
        
        return response
    
    def reset_conversation(self):
        """Reset the conversation history."""
        # Keep only the system prompt if it exists
        if self.conversation_history and self.conversation_history[0]["role"] == "system":
            self.conversation_history = [self.conversation_history[0]]
        else:
            self.conversation_history = []

def interactive_chat():
    """Run an interactive chat session."""
    print("Interactive ChatBot")
    print("=" * 50)
    print("Type 'quit' to exit, 'reset' to start a new conversation")
    print()
    
    # Create chatbot with personality
    system_prompt = """You are a helpful, friendly, and knowledgeable assistant. 
    You should be conversational and engaging while providing accurate and useful information. 
    Keep responses concise but informative."""
    
    bot = ChatBot(system_prompt)
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            elif user_input.lower() == 'reset':
                bot.reset_conversation()
                print("Conversation reset!")
                continue
            elif not user_input:
                continue
            
            print("Bot: ", end="")
            response = bot.chat(user_input)
            print(response)
            print()
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

def specialized_chatbot_examples():
    """Examples of specialized chatbots with different personalities."""
    print("Specialized Chatbot Examples")
    print("=" * 50)
    
    # 1. Coding Assistant
    print("\n1. Coding Assistant Bot:")
    coding_bot = ChatBot("""You are a programming expert and tutor. You help people learn to code 
    and solve programming problems. You provide clear explanations and well-commented code examples.""")
    
    response = coding_bot.chat("How do I sort a list in Python?")
    print(f"User: How do I sort a list in Python?")
    print(f"Bot: {response}")
    
    # 2. Creative Writing Assistant
    print("\n2. Creative Writing Assistant Bot:")
    writing_bot = ChatBot("""You are a creative writing assistant. You help with storytelling, 
    character development, plot ideas, and writing techniques. You're encouraging and constructive.""")
    
    response = writing_bot.chat("I'm stuck on my novel. My main character feels flat. Any suggestions?")
    print(f"User: I'm stuck on my novel. My main character feels flat. Any suggestions?")
    print(f"Bot: {response}")
    
    # 3. Study Buddy
    print("\n3. Study Buddy Bot:")
    study_bot = ChatBot("""You are a study buddy who helps students learn. You break down complex 
    topics into simple explanations, create study plans, and use analogies to make learning fun.""")
    
    response = study_bot.chat("Can you explain photosynthesis in simple terms?")
    print(f"User: Can you explain photosynthesis in simple terms?")
    print(f"Bot: {response}")

def conversation_memory_example():
    """Example showing how the bot remembers conversation context."""
    print("\n\nConversation Memory Example")
    print("=" * 50)
    
    bot = ChatBot("You are a helpful assistant with a good memory for details.")
    
    # First message
    response1 = bot.chat("My name is Alice and I'm a software engineer.")
    print("User: My name is Alice and I'm a software engineer.")
    print(f"Bot: {response1}")
    
    # Second message - bot should remember the name and profession
    response2 = bot.chat("What's my profession again?")
    print("\nUser: What's my profession again?")
    print(f"Bot: {response2}")
    
    # Third message - test more memory
    response3 = bot.chat("What did I tell you about myself?")
    print("\nUser: What did I tell you about myself?")
    print(f"Bot: {response3}")

def main():
    """Run chatbot examples."""
    try:
        choice = input("Choose an option:\n1. Interactive Chat\n2. Specialized Bot Examples\n3. Memory Example\nEnter (1/2/3): ").strip()
        
        if choice == "1":
            interactive_chat()
        elif choice == "2":
            specialized_chatbot_examples()
        elif choice == "3":
            conversation_memory_example()
        else:
            print("Running all examples...")
            specialized_chatbot_examples()
            conversation_memory_example()
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()