# 📦 Installation Guide - TTZ.KT AI Platform

Complete step-by-step installation guide for Windows, macOS, and Linux.

**Repository**: https://github.com/tharun-kumar-22/TTZ_Ready_To_Go_AI_platform

---

## 📋 **Table of Contents**

1. [Prerequisites](#prerequisites)
2. [Windows Installation](#windows-installation)
3. [macOS Installation](#macos-installation)
4. [Linux Installation](#linux-installation)
5. [Verification](#verification)
6. [First Run](#first-run)
7. [Troubleshooting](#troubleshooting)
8. [Choosing Models](#choosing-models)

---

## 🔧 **Prerequisites**

Before installation, ensure you have:

- ✅ **Python 3.8 or higher** installed
- ✅ **pip** (Python package manager)
- ✅ **Git** (for cloning repository)
- ✅ **8GB+ RAM** (16GB recommended)
- ✅ **5GB+ free disk space**

---

## 💻 **Windows Installation**

### **Step 1: Install Python**

1. Download Python from [python.org](https://www.python.org/downloads/)
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Verify installation:
```cmd
   python --version
```
   Should show: `Python 3.8.x` or higher

### **Step 2: Install Ollama**

1. Download Ollama from [ollama.ai](https://ollama.ai/download)
2. Run the installer (`OllamaSetup.exe`)
3. Ollama will start automatically
4. Verify installation:
```cmd
   ollama --version
```

### **Step 3: Download Project**

**Option A: Using Git**
```cmd
git clone https://github.com/tharun-kumar-22/TTZ_Ready_To_Go_AI_platform.git
cd TTZ_Ready_To_Go_AI_platform
```

**Option B: Download ZIP**
1. Go to https://github.com/tharun-kumar-22/TTZ_Ready_To_Go_AI_platform
2. Click "Code" → "Download ZIP"
3. Extract to your desired location
4. Open Command Prompt in that folder

### **Step 4: Install Dependencies**
```cmd
pip install -r requirements.txt
```

This will install all required Python packages (~5 minutes).

### **Step 5: Download AI Models**

Download at least one model:
```cmd
ollama pull qwen2.5:7b
```

**Recommended models for Windows:**
```cmd
ollama pull qwen2.5:7b     # Best balance (4.7 GB)
ollama pull llama3.2       # Fast (2.0 GB)
ollama pull phi3           # Lightweight (2.3 GB)
```

### **Step 6: Run the Application**
```cmd
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## 🍎 **macOS Installation**

### **Step 1: Install Python**

**Option A: Using Homebrew (Recommended)**
```bash
brew install python@3.11
```

**Option B: Download from python.org**
1. Download from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. Verify:
```bash
   python3 --version
```

### **Step 2: Install Ollama**

1. Download Ollama from [ollama.ai](https://ollama.ai/download)
2. Open the `.dmg` file
3. Drag Ollama to Applications
4. Launch Ollama from Applications
5. Verify:
```bash
   ollama --version
```

### **Step 3: Download Project**
```bash
git clone https://github.com/tharun-kumar-22/TTZ_Ready_To_Go_AI_platform.git
cd TTZ_Ready_To_Go_AI_platform
```

### **Step 4: Install Dependencies**
```bash
pip3 install -r requirements.txt
```

### **Step 5: Download Models**
```bash
ollama pull qwen2.5:7b
```

### **Step 6: Run Application**
```bash
streamlit run app.py
```

---

## 🐧 **Linux Installation**

### **Step 1: Install Python**

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip git
```

**Fedora:**
```bash
sudo dnf install python3 python3-pip git
```

**Arch:**
```bash
sudo pacman -S python python-pip git
```

### **Step 2: Install Ollama**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

Start Ollama service:
```bash
ollama serve
```

### **Step 3: Download Project**
```bash
git clone https://github.com/tharun-kumar-22/TTZ_Ready_To_Go_AI_platform.git
cd TTZ_Ready_To_Go_AI_platform
```

### **Step 4: Install Dependencies**
```bash
pip3 install -r requirements.txt
```

### **Step 5: Download Models**
```bash
ollama pull qwen2.5:7b
```

### **Step 6: Run Application**
```bash
streamlit run app.py
```

---

## ✅ **Verification**

### **Check Ollama is Running**
```bash
curl http://localhost:11434
```

Should return: `Ollama is running`

### **Check Available Models**
```bash
ollama list
```

Should show your downloaded models.

### **Check Python Packages**
```bash
pip list | grep streamlit
pip list | grep langchain
```

Both should be installed.

---

## 🚀 **First Run**

### **1. Start the Application**
```bash
streamlit run app.py
```

You'll see:
```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
```

### **2. Open Browser**

- Automatically opens, or visit `http://localhost:8501`

### **3. Select Model**

- In sidebar, choose from your downloaded models
- Start with `qwen2.5:7b`

### **4. Upload Documents**

- Click "Choose files"
- Select PDF, DOCX, CSV, etc.
- Click "🚀 Process All Files"

### **5. Start Chatting!**

- Type questions in chat box
- Get instant answers from your documents

## 🔍 **Troubleshooting**

### **Issue: "Module not found" error**

**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

### **Issue: "Connection refused to localhost:11434"**

**Solution:**
1. Check Ollama is running:
```bash
   ollama serve
```
2. Verify in browser: `http://localhost:11434`
3. Restart Ollama if needed

### **Issue: "Model 'qwen2.5:7b' not found"**

**Solution:**
```bash
ollama pull qwen2.5:7b
```

### **Issue: Slow performance**

**Solutions:**
1. Use smaller model:
```bash
   ollama pull qwen2.5:3b
```
2. Close other applications
3. Check GPU availability:
```bash
   python -c "import torch; print(torch.cuda.is_available())"
```

### **Issue: Port 8501 already in use**

**Solution:**
```bash
streamlit run app.py --server.port 8502
```

### **Issue: "CUDA out of memory" (GPU users)**

**Solution:**
Use CPU-only mode by editing `rag_engine.py`:
```python
device = 'cpu'  # Change from 'cuda' to 'cpu'
```

### **Issue: Import error with 'unstructured'**

**Solution:**
```bash
pip install "unstructured[local-inference]"
```

### **Issue: Windows - "python not recognized"**

**Solution:**
1. Reinstall Python with "Add to PATH" checked
2. Or use full path: `C:\Python311\python.exe`

### **Issue: macOS - "Permission denied"**

**Solution:**
```bash
chmod +x app.py
python3 app.py
```

---

## 🤖 **Choosing Models**

### **By Size (Disk Space)**

| Model | Size | Speed | Quality |
|-------|------|-------|---------|
| `qwen2.5:3b` | 2.0 GB | ⚡⚡⚡ | ⭐⭐⭐ |
| `phi3:latest` | 2.3 GB | ⚡⚡⚡ | ⭐⭐⭐ |
| `llama3.2:latest` | 2.0 GB | ⚡⚡⚡ | ⭐⭐⭐⭐ |
| `qwen2.5:7b` | 4.7 GB | ⚡⚡ | ⭐⭐⭐⭐⭐ |
| `llama3.1:latest` | 4.7 GB | ⚡⚡ | ⭐⭐⭐⭐⭐ |
| `mistral:latest` | 4.1 GB | ⚡⚡ | ⭐⭐⭐⭐ |
| `deepseek-r1:8b` | 4.9 GB | ⚡ | ⭐⭐⭐⭐⭐ |

### **By Use Case**

**General Document Q&A:**
```bash
ollama pull qwen2.5:7b
```

**Fast Responses:**
```bash
ollama pull llama3.2
```

**Advanced Reasoning:**
```bash
ollama pull deepseek-r1:8b
```

**Coding/Technical:**
```bash
ollama pull qwen2.5-coder
```

**Low RAM Systems:**
```bash
ollama pull phi3
```

### **Download Multiple Models**
```bash
ollama pull qwen2.5:7b
ollama pull llama3.2
ollama pull phi3
```

Switch between them instantly in the app!

---

## 🔄 **Updating**

### **Update Application**
```bash
cd TTZ_Ready_To_Go_AI_platform
git pull origin main
pip install -r requirements.txt --upgrade
```

### **Update Models**
```bash
ollama pull qwen2.5:7b
```

---

## 🗑️ **Uninstalling**

### **Remove Application**

Simply delete the folder:
```bash
rm -rf TTZ_Ready_To_Go_AI_platform
```

### **Remove Models**
```bash
ollama rm qwen2.5:7b
```

### **Uninstall Ollama**

**Windows:** Control Panel → Uninstall Programs → Ollama

**macOS:** Delete from Applications folder

**Linux:**
```bash
sudo rm /usr/local/bin/ollama
```

---

## 📞 **Need Help?**

- **Documentation**: [README.md](README.md)
- **Issues**: [GitHub Issues](https://github.com/tharun-kumar-22/TTZ_Ready_To_Go_AI_platform/issues)
- **Discussions**: [GitHub Discussions](https://github.com/tharun-kumar-22/TTZ_Ready_To_Go_AI_platform/discussions)

---

**Installation complete! Start chatting with your documents! 🎉**

**Repository**: https://github.com/tharun-kumar-22/TTZ_Ready_To_Go_AI_platform
