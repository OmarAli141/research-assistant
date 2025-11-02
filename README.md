# 🔍 Research Assistant

An intelligent research assistant that searches the web, scrapes content, and generates comprehensive reports using AI.

## Features

- 🔍 **Web Search**: Uses DuckDuckGo to find relevant information
- 📄 **Content Scraping**: Extracts text from web pages
- 🤖 **AI Summarization**: Uses Ollama with deepseek-r1 to generate reports
- 🎨 **Dual Interface**: Both command-line and graphical user interfaces
- 📊 **Comprehensive Reports**: Generates well-structured Markdown reports

## Requirements

- Python 3.8+
- Ollama installed and running locally
- deepseek-r1:1.5b model pulled in Ollama

## Installation

1. Clone this repository or download the files

2. Install required packages:
```bash
pip install langchain-community langchain-core beautifulsoup4 requests duckduckgo-search
```

3. Install and run Ollama:
   - Download from [ollama.ai](https://ollama.ai)
   - Pull the deepseek-r1 model:
   ```bash
   ollama pull deepseek-r1:1.5b
   ```
   - Make sure Ollama is running on localhost:11434

## Usage

### GUI Mode (Recommended)

Run the graphical interface:
```bash
python research_assistant_gui.py
```

Features:
- Clean, modern interface
- Real-time status updates
- Displays research progress
- Easy-to-use text input and display

### Command-Line Interface

Run the CLI version:
```bash
python research_assistant.py
```

Features:
- Interactive menu
- Simple text-based interface
- Keyboard shortcuts support

## How It Works

1. **Search**: Queries DuckDuckGo for relevant URLs based on your question
2. **Scrape**: Extracts text content from found web pages
3. **Summarize**: Generates individual summaries for each source
4. **Synthesize**: Combines all summaries into a comprehensive final report

## Example Usage

**Question**: "What are the benefits of renewable energy?"

The assistant will:
1. Search for relevant articles about renewable energy
2. Scrape content from multiple sources
3. Generate summaries from each source
4. Create a comprehensive report with all information synthesized

## Architecture

- `ResearchAssistant` class: Core functionality
  - `search_web()`: Web search using DuckDuckGo
  - `scrape_text()`: Content extraction from URLs
  - `summarize_text()`: AI-powered summarization
  - `research_topic()`: Complete research pipeline

- `ResearchAssistantGUI` class: Tkinter-based graphical interface
- CLI: Interactive command-line interface

## Troubleshooting

**"Connection refused" error:**
- Make sure Ollama is running: `ollama list`
- Verify it's accessible on localhost:11434

**"Model not found" error:**
- Pull the required model: `ollama pull deepseek-r1:1.5b`

**Search not working:**
- Check your internet connection
- DuckDuckGo may be rate-limiting (wait a few minutes)

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Uses [Ollama](https://ollama.ai) for local AI inference
- [LangChain](https://langchain.com) for LLM integration
- [DuckDuckGo](https://duckduckgo.com) for web search

