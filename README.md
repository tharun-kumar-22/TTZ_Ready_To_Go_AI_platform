# 🚀 TTZ.KT AI Platform 2025 - Local Document Assistant

![Version](https://img.shields.io/badge/version-8.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Mac%20%7C%20Linux-lightgrey)

**100% Free | 100% Local | 100% Private**

Chat with your documents using powerful AI models - completely offline and private. No API keys, no internet required, no data leaves your computer.

---

## ✨ **Features**

- 🤖 **19 AI Models** - Qwen, DeepSeek, Llama, Mistral, Gemma, Phi, GPT-OSS
- 📄 **13+ File Formats** - PDF, DOCX, CSV, XLSX, Images, JSON, XML, YAML and more
- 💾 **100% Local Processing** - All data stays on your computer
- 🔒 **Complete Privacy** - No internet connection needed after setup
- 💰 **Zero Cost** - No API fees, completely free forever
- ⚡ **Instant Model Switching** - Change AI models without reprocessing documents
- 🎯 **Smart Retrieval** - Advanced RAG (Retrieval Augmented Generation) technology
- 💬 **Conversational** - Chat naturally with your documents

---

## 📋 **What Can You Do?**

- 📚 **Research**: Analyze research papers, extract key information
- 💼 **Business**: Process reports, analyze data, extract insights
- 📖 **Study**: Learn from textbooks, create summaries, ask questions
- 📊 **Data Analysis**: Query CSV/Excel files naturally
- 🔍 **Document Search**: Find information across multiple documents instantly
- 📝 **Content Creation**: Extract quotes, generate summaries

---

## 🎯 **Supported File Formats**

| Category | Formats |
|----------|---------|
| 📄 **Documents** | PDF, DOCX, DOC, TXT, RTF, MD |
| 📊 **Spreadsheets** | CSV, XLSX, XLS, ODS |
| 🖼️ **Images** | PNG, JPG, JPEG, BMP, TIFF, GIF |
| 💾 **Data Files** | JSON, XML, YAML, YML |

---

## 🚀 **Quick Start**

### **Prerequisites**
- **Python 3.8+** installed
- **Ollama** installed and running
- **At least one Ollama model** downloaded

### **Installation (5 minutes)**

1. **Download this project**
```bash
   git clone https://github.com/tharun-kumar-22/TTZ_Ready_To_Go_AI_platform.git
   cd TTZ_Ready_To_Go_AI_platform
```

2. **Install Python dependencies**
```bash
   pip install -r requirements.txt
```

3. **Download at least one Ollama model**
```bash
   ollama pull qwen2.5:7b
```

4. **Run the application**
```bash
   streamlit run app.py
```

5. **Open your browser** - The app will automatically open at `http://localhost:8501`

**That's it! 🎉**

---

## 📖 **How to Use**

### **Step 1: Select AI Model**
Choose from your downloaded Ollama models in the sidebar.

**Recommended models:**
- `qwen2.5:7b` - Best balance of speed and accuracy
- `llama3.2:latest` - Fast and efficient
- `deepseek-r1:8b` - Advanced reasoning capabilities

### **Step 2: Upload Documents**
- Click "Choose files" in the sidebar
- Select one or multiple files (PDF, DOCX, CSV, etc.)
- Click "🚀 Process All Files"

### **Step 3: Ask Questions**
Type your questions in the chat box. Examples:
- "What are the main points in this document?"
- "Summarize the findings in chapter 3"
- "What are all the questions mentioned in the PDF?"
- "Compare the data in these spreadsheets"

### **Step 4: Switch Models (Optional)**
Change AI models anytime without re-uploading documents!

---

## 🤖 **Available AI Models**

The app supports **19 Ollama models** across 8 families:

### **🌟 Qwen Family (7 models)**
- `qwen3:latest`, `qwen3:8b` - Latest 2025 models
- `qwen2.5:latest`, `qwen2.5:7b`, `qwen2.5:3b` - Stable versions
- `qwen3-coder:latest`, `qwen2.5-coder:latest` - Code specialists

### **🧠 DeepSeek (2 models)**
- `deepseek-r1:latest`, `deepseek-r1:8b` - Advanced reasoning

### **🦙 Llama (2 models)**
- `llama3.2:latest`, `llama3.1:latest` - Meta's powerful models

### **🔥 Mistral (1 model)**
- `mistral:latest` - Fast and powerful

### **💎 Gemma (2 models)**
- `gemma3:latest`, `gemma2:latest` - Google's efficient models

### **🧠 Phi (3 models)**
- `phi4:latest`, `phi3.5:latest`, `phi3:latest` - Microsoft's compact models

### **🤖 GPT-OSS (2 models)**
- `gpt-oss:latest`, `gpt-oss:20b` - OpenAI-style open source

**Download models with:**
```bash
ollama pull model-name
```

---

## 💡 **Tips for Best Results**

1. **Model Selection**
   - Start with `qwen2.5:7b` for balanced performance
   - Use `deepseek-r1:8b` for complex reasoning tasks
   - Try `llama3.2` for faster responses

2. **Document Upload**
   - Upload related documents together for better context
   - Clear and well-formatted documents work best
   - Process multiple files at once to compare information

3. **Asking Questions**
   - Be specific in your questions
   - Ask follow-up questions for deeper insights
   - Use "list all..." for comprehensive answers

4. **Performance**
   - First response may be slower (model loading)
   - Subsequent queries are much faster
   - Switch models without reprocessing for instant comparison

---

## 🔧 **System Requirements**

### **Minimum**
- **CPU**: 4 cores
- **RAM**: 8 GB
- **Storage**: 5 GB free (for models)
- **OS**: Windows 10/11, macOS 10.15+, or Linux

### **Recommended**
- **CPU**: 8+ cores or GPU (NVIDIA/AMD)
- **RAM**: 16 GB+
- **Storage**: 20 GB+ (for multiple models)
- **GPU**: CUDA-compatible (optional, for faster performance)

---

## 🛠️ **Troubleshooting**

### **"Connection refused" error**
- Ensure Ollama is running: `ollama serve`
- Check Ollama is at `http://localhost:11434`

### **"Model not found" error**
- Download the model first: `ollama pull qwen2.5:7b`
- Check available models: `ollama list`

### **Slow performance**
- Use smaller models (`qwen2.5:3b`, `phi3`)
- Close other applications
- Use GPU if available

### **Import errors**
```bash
pip install -r requirements.txt --upgrade
```

**For detailed troubleshooting**, see [INSTALL.md](INSTALL.md)

---

## 🔒 **Privacy & Security**

- ✅ **No Internet Required** - Works completely offline after setup
- ✅ **No Data Collection** - Zero telemetry or tracking
- ✅ **No Cloud Storage** - All files processed locally in memory
- ✅ **No API Keys** - No external services or accounts needed
- ✅ **Temporary Files** - Deleted immediately after processing
- ✅ **Your Data, Your Computer** - Complete control and privacy

---

## 📚 **Documentation**

- [Installation Guide](INSTALL.md) - Detailed setup instructions
- [Troubleshooting](INSTALL.md#troubleshooting) - Common issues and solutions
- [Model Guide](INSTALL.md#choosing-models) - Which model to use

---

## 🤝 **Contributing**

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Share your experience

---

## 📄 **License**

MIT License - Free to use for personal and commercial projects.

---

## 🌟 **Star This Project**

If you find this useful, please give it a ⭐ on GitHub!

---

## 📞 **Support**

- **Issues**: [GitHub Issues](https://github.com/tharun-kumar-22/TTZ_Ready_To_Go_AI_platform/issues)
- **Discussions**: [GitHub Discussions](https://github.com/tharun-kumar-22/TTZ_Ready_To_Go_AI_platform/discussions)

---

## 🙏 **Acknowledgments**

Built with:
- [Ollama](https://ollama.ai/) - Local LLM runtime
- [LangChain](https://www.langchain.com/) - LLM framework
- [Streamlit](https://streamlit.io/) - Web interface
- [FAISS](https://github.com/facebookresearch/faiss) - Vector search
- [HuggingFace](https://huggingface.co/) - Embeddings

---

**Made with ❤️ for the local AI community**

**Repository**: https://github.com/tharun-kumar-22/TTZ_Ready_To_Go_AI_platform

---

*Last updated: October 2025*
