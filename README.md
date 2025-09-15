# OpenAI API Project

A comprehensive Python project demonstrating how to use the OpenAI API for various natural language processing tasks including chat completions, text generation, summarization, translation, and more.

## 🚀 Features

- **Easy-to-use OpenAI API wrapper** with configuration management
- **Interactive chatbot** with conversation memory
- **Text generation examples** including creative writing, summarization, and translation
- **Code generation** demonstrations
- **Specialized chatbots** for different use cases
- **Environment-based configuration** for security
- **Well-documented code** with examples

## 📁 Project Structure

```
openai-project/
├── src/
│   └── openai_client.py          # Main OpenAI API wrapper class
├── examples/
│   ├── text_generation.py        # Text generation examples
│   └── chatbot.py                # Interactive chatbot examples
├── config/                       # Configuration files (if needed)
├── requirements.txt              # Python dependencies
├── .env.template                 # Environment variables template
├── .gitignore                   # Git ignore file
└── README.md                    # This file
```

## 🛠️ Setup

### Prerequisites

- Python 3.7 or higher
- OpenAI API key (get one from [OpenAI Platform](https://platform.openai.com/))

### Installation

1. **Clone or download this project**
   ```bash
   git clone <repository-url>
   cd openai-project
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the template
   cp .env.template .env
   
   # Edit .env and add your OpenAI API key
   # OPENAI_API_KEY=your_actual_api_key_here
   ```

### Configuration

Edit the `.env` file with your settings:

```env
# Required: Your OpenAI API key
OPENAI_API_KEY=sk-your-api-key-here

# Optional: Organization ID (if using organization-based billing)
# OPENAI_ORG_ID=org-your-org-id-here

# Model Configuration
DEFAULT_MODEL=gpt-3.5-turbo
MAX_TOKENS=1500
TEMPERATURE=0.7
```

## 🎯 Usage

### Basic Usage

```python
from src.openai_client import OpenAIClient

# Initialize client
client = OpenAIClient()

# Simple completion
response = client.simple_completion("Explain quantum computing in simple terms")
print(response)

# Chat with system prompt
response = client.conversation(
    system_prompt="You are a helpful Python tutor",
    user_message="How do I create a list in Python?"
)
print(response)
```

### Running Examples

1. **Basic OpenAI client test**
   ```bash
   python src/openai_client.py
   ```

2. **Text generation examples**
   ```bash
   python examples/text_generation.py
   ```

3. **Interactive chatbot**
   ```bash
   python examples/chatbot.py
   ```

## 📚 Examples

### Text Generation

The project includes examples for:
- **Creative writing** - Generate stories, poems, and creative content
- **Text summarization** - Summarize long documents
- **Language translation** - Translate between different languages  
- **Code generation** - Generate code snippets and functions

### Chatbot Features

- **Interactive chat** - Real-time conversation with the AI
- **Conversation memory** - Maintains context throughout the conversation
- **Specialized bots** - Different personalities for specific use cases:
  - Coding assistant
  - Creative writing helper
  - Study buddy

### Example Code Snippets

#### Simple Completion
```python
client = OpenAIClient()
response = client.simple_completion("Write a haiku about programming")
```

#### Chat with Memory
```python
messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hello! How can I help you today?"},
    {"role": "user", "content": "What did I just say?"}
]
response = client.chat_completion(messages)
```

## 🔧 API Reference

### OpenAIClient Class

#### Constructor
- `OpenAIClient(api_key=None)` - Initialize with optional API key

#### Methods

- `simple_completion(prompt, **kwargs)` - Generate completion from prompt
- `chat_completion(messages, model=None, max_tokens=None, temperature=None)` - Chat completion with message history
- `conversation(system_prompt, user_message, **kwargs)` - Simple system + user message

#### Parameters
- `model` - OpenAI model to use (default: gpt-3.5-turbo)
- `max_tokens` - Maximum tokens in response (default: 1500)
- `temperature` - Creativity level 0.0-1.0 (default: 0.7)

## 🔐 Security

- **Never commit your `.env` file** - It contains your API key
- **Use environment variables** for sensitive configuration
- **Regenerate API keys** if accidentally exposed
- **Monitor API usage** to prevent unexpected charges

## 💡 Tips

1. **Start with lower cost models** like `gpt-3.5-turbo` for development
2. **Use appropriate temperature settings**:
   - Low (0.0-0.3) for factual, consistent responses
   - Medium (0.4-0.7) for balanced creativity
   - High (0.8-1.0) for creative, varied responses
3. **Manage token limits** to control costs
4. **Use system prompts** to set consistent behavior
5. **Handle errors gracefully** in production code

## 🚨 Common Issues

### API Key Issues
- **Error: "OpenAI API key not found"**
  - Make sure `.env` file exists and contains `OPENAI_API_KEY`
  - Check that python-dotenv is installed

### Rate Limiting
- **Error: "Rate limit exceeded"**
  - You're making requests too quickly
  - Add delays between requests or implement retry logic

### Token Limits
- **Error: "Token limit exceeded"**
  - Reduce `max_tokens` parameter
  - Shorten your input prompts

## 📈 Next Steps

Consider extending this project with:

- **Streaming responses** for real-time output
- **Function calling** for tool integration
- **Image generation** using DALL-E
- **Audio transcription** using Whisper
- **Web interface** using Flask or Streamlit
- **Database integration** for conversation history
- **Custom fine-tuning** for specific use cases

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [OpenAI Python Library](https://github.com/openai/openai-python)
- [OpenAI Pricing](https://openai.com/pricing)
- [Best Practices Guide](https://platform.openai.com/docs/guides/production-best-practices)

## 📞 Support

If you encounter issues:
1. Check the [Common Issues](#-common-issues) section
2. Review the OpenAI API documentation
3. Check your API key and billing status
4. Create an issue in this repository

---

**Happy coding with OpenAI! 🤖✨**