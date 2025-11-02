# Usage Guide

## Quick Start

### Option 1: Graphical Interface (Recommended) 🖥️

```bash
python research_assistant_gui.py
```

**Features:**
- Modern, user-friendly interface
- Large text display area for reports
- Real-time status updates
- Progress indicators
- Error handling with helpful messages

**How to use:**
1. Launch the application
2. Wait for "Ready" status
3. Enter your research question
4. Click "🔍 Research" or press Enter
5. View your comprehensive report
6. Use "🗑️ Clear" to start over

### Option 2: Command-Line Interface 💻

```bash
python research_assistant.py
```

**Features:**
- Simple text-based menu
- Keyboard-driven navigation
- Status messages during processing
- Multiple question capability in one session

**How to use:**
1. Run the script
2. Enter 1 to ask a question
3. Type your research question
4. Wait for the report
5. Enter 2 to exit

## Example Questions

Try these example research questions:

1. "What are the benefits of renewable energy?"
2. "How does machine learning work?"
3. "What is the capital of France?"
4. "Explain the water cycle"
5. "What are the main causes of climate change?"

## Tips for Best Results

- **Be specific**: More specific questions yield better results
- **Be concise**: Keep questions under 20 words for best performance
- **Wait patiently**: Research takes time (30-60 seconds typically)
- **Check Ollama**: Make sure Ollama is running for AI features

## Keyboard Shortcuts

### GUI:
- `Enter`: Submit question
- `Ctrl+C`: Cancel operation (Windows/Linux)
- Click buttons with mouse or Tab navigation

### CLI:
- Type number to select option
- `Ctrl+C`: Exit program

## Troubleshooting

### "Connection refused" Error
```bash
# Start Ollama if not running
ollama serve

# Check if running
ollama list
```

### "Model not found" Error
```bash
# Pull the required model
ollama pull deepseek-r1:1.5b
```

### Slow Performance
- Reduce number of search results in code
- Check internet connection
- Ensure Ollama has sufficient resources

### No Search Results
- Check internet connection
- Try a different question
- DuckDuckGo might be rate-limiting (wait a few minutes)

## Configuration

Edit `research_assistant.py` to customize:

- **Number of search results** (line 24): Change `num_results` default
- **AI model** (line 16): Change the Ollama model
- **Temperature** (line 17): Adjust creativity (0.0-1.0)

## Advanced Usage

### Programmatic API

Use the `ResearchAssistant` class in your own code:

```python
from research_assistant import ResearchAssistant

assistant = ResearchAssistant()
report = assistant.research_topic("Your question here")
print(report)
```

### Custom Search Results

```python
urls = assistant.search_web("query", num_results=5)
```

### Direct Text Scraping

```python
text = assistant.scrape_text("https://example.com")
```

### Individual Summarization

```python
summary = assistant.summarize_text(text, question="What is this about?")
```

## Next Steps

1. Read the README.md for project overview
2. Check requirements.txt for dependencies
3. Customize the code for your needs
4. Share feedback and improvements!

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review error messages carefully
3. Verify all dependencies are installed
4. Ensure Ollama is properly configured

