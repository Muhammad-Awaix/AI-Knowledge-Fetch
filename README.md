# AI News Fetcher and Summarizer

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A powerful AI-powered application that fetches the latest AI news from top sources and provides intelligent summaries using advanced language models.

## 🌟 Features

- **Real-time News Fetching**: Automatically retrieves latest AI articles from:
  - O'Reilly Radar
  - Hugging Face Blog
  - TensorFlow Blog
- **Intelligent Summarization**: Uses LangChain and Groq for high-quality article summaries
- **Web Interface**: Beautiful Streamlit-based UI for easy interaction
- **Clean Data Processing**: HTML stripping and text cleaning for readable summaries
- **Configurable Prompts**: Customizable summarization prompts for different use cases

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ai-news-fetcher
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file with your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

### Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** to `http://localhost:8501`

3. **Fetch and summarize news** with a single click!

## 📁 Project Structure

```
ai-news-fetcher/
├── app.py              # Main Streamlit application
├── fetcher.py          # RSS feed fetching logic
├── summrizer.py        # AI-powered summarization
├── prompts.py          # Summarization prompts
├── requirements.txt    # Python dependencies
├── template.sh         # Utility script
└── README.md          # Project documentation
```

## 🔧 Configuration

### Environment Variables

- `GROQ_API_KEY`: Your Groq API key for LLM services

### Customization

- Modify `prompts.py` to change summarization behavior
- Update feed URLs in `fetcher.py` for different sources
- Adjust summary length in the summarization logic

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Feedparser](https://github.com/kurtmckee/feedparser) for RSS parsing
- [LangChain](https://github.com/langchain-ai/langchain) for LLM orchestration
- [Streamlit](https://streamlit.io/) for the web interface
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing

## 📞 Support

If you find this project helpful, please give it a ⭐️!

For questions or issues, please open an [issue](https://github.com/your-username/ai-news-fetcher/issues) on GitHub.</content>
<parameter name="filePath">d:\Ai_update\README.md
