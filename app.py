import streamlit as st
import os
from rag_engine import RAGEngine
import time

FORMAT_ICONS = {
    'pdf': '📕', 'docx': '📘', 'doc': '📘', 'txt': '📄', 'rtf': '📋', 'md': '📄',
    'csv': '📊', 'xlsx': '📈', 'xls': '📈', 'ods': '📊',
    'png': '🖼️', 'jpg': '🖼️', 'jpeg': '🖼️', 'bmp': '🖼️', 'tiff': '🖼️', 'gif': '🖼️',
    'json': '💾', 'xml': '💾', 'yaml': '💾', 'yml': '💾'
}

st.set_page_config(
    page_title="TTZ.KT AI - Ollama 2025",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem 0;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3rem;
        font-weight: bold;
    }
    .model-info {
        background: #e8f4f8;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .memory-badge {
        background: #4CAF50;
        color: white;
        padding: 0.3rem 0.6rem;
        border-radius: 5px;
        font-size: 0.8rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

if 'rag_engine' not in st.session_state:
    st.session_state.rag_engine = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'document_processed' not in st.session_state:
    st.session_state.document_processed = False
if 'processed_files' not in st.session_state:
    st.session_state.processed_files = []
if 'current_model' not in st.session_state:
    st.session_state.current_model = "qwen2.5:7b"

st.markdown('<h1 class="main-header">🚀 TTZ.KT AI Platform 2025</h1>', unsafe_allow_html=True)
st.markdown("### *Multi-Format Document Assistant - Your Models*")
st.markdown('<span class="memory-badge">💾 Local Processing - 100% Private</span>', unsafe_allow_html=True)
st.markdown("---")

with st.sidebar:
    st.header("⚙️ Configuration")
    
    st.success("✅ Ollama Local")
    st.caption("🔗 http://localhost:11434")
    
    st.markdown("---")
    
    st.subheader("🤖 Select AI Model")
    
    available_models = {
        "🌟 Qwen 3 (Latest 2025)": [
            "qwen3:latest",
            "qwen3:8b",
            "qwen3-coder:latest"
        ],
        "⭐ Qwen 2.5 (Stable)": [
            "qwen2.5:latest",
            "qwen2.5:7b",
            "qwen2.5:3b",
            "qwen2.5-coder:latest"
        ],
        "🧠 DeepSeek (Reasoning)": [
            "deepseek-r1:latest",
            "deepseek-r1:8b"
        ],
        "🦙 Llama (Meta)": [
            "llama3.2:latest",
            "llama3.1:latest"
        ],
        "🔥 Mistral": [
            "mistral:latest"
        ],
        "💎 Gemma (Google)": [
            "gemma3:latest",
            "gemma2:latest"
        ],
        "🧠 Phi (Microsoft)": [
            "phi4:latest",
            "phi3.5:latest",
            "phi3:latest"
        ],
        "🤖 GPT-OSS (OpenAI Style)": [
            "gpt-oss:latest",
            "gpt-oss:20b"
        ]
    }
    
    all_models = []
    model_labels = []
    for category, models in available_models.items():
        for model in models:
            all_models.append(model)
            clean_category = category.split(" (")[0]
            model_labels.append(f"{clean_category}: {model}")
    
    selected_model_idx = st.selectbox(
        "Choose your model",
        range(len(all_models)),
        format_func=lambda i: model_labels[i],
        index=all_models.index(st.session_state.current_model) if st.session_state.current_model in all_models else 0
    )
    
    selected_model = all_models[selected_model_idx]
    
    model_info = {
        "qwen3": "🌟 Latest Qwen 3 (2025)",
        "qwen2.5": "⭐ Stable & reliable",
        "deepseek-r1": "🧠 Advanced reasoning",
        "llama3.2": "🦙 Fast & efficient",
        "llama3.1": "🦙 Powerful Llama",
        "mistral": "🔥 Fast performance",
        "gemma3": "💎 Latest Gemma 3",
        "gemma2": "💎 Stable Gemma 2",
        "phi4": "🧠 Latest Phi 4 (2025)",
        "phi3": "🧠 Efficient Phi 3",
        "gpt-oss": "🤖 OpenAI-style (Open Source)"
    }
    
    info_text = "📋 Ollama model"
    for key, info in model_info.items():
        if selected_model.startswith(key):
            info_text = info
            break
    
    st.markdown(f'<div class="model-info">📌 {info_text}</div>', unsafe_allow_html=True)
    
    if st.session_state.rag_engine and selected_model != st.session_state.current_model:
        if st.button("🔄 Switch Model", type="secondary"):
            with st.spinner(f"Switching to {selected_model}..."):
                try:
                    st.session_state.rag_engine.switch_model(selected_model)
                    st.session_state.current_model = selected_model
                    st.success(f"✅ Switched to {selected_model}")
                    time.sleep(0.5)
                    st.rerun()
                except Exception as e:
                    st.error(f"⚠️ Error: {str(e)}")
    
    st.markdown("---")
    
    st.header("📄 Supported Formats")
    st.markdown('<span class="memory-badge">💾 Memory Only</span>', unsafe_allow_html=True)
    
    with st.expander("View all formats"):
        st.markdown("""
        **📄 Documents:** PDF, DOCX, TXT, RTF, MD  
        **📊 Spreadsheets:** CSV, XLSX, XLS, ODS  
        **🖼️ Images:** PNG, JPG, JPEG, BMP, TIFF  
        **💾 Data:** JSON, XML, YAML
        """)
    
    st.markdown("---")
    
    st.header("📤 Upload & Process")
    
    supported_extensions = [
        'pdf', 'docx', 'doc', 'txt', 'rtf', 'md',
        'csv', 'xlsx', 'xls', 'ods',
        'png', 'jpg', 'jpeg', 'bmp', 'tiff', 'gif',
        'json', 'xml', 'yaml', 'yml'
    ]
    
    uploaded_files = st.file_uploader(
        "Choose files",
        type=supported_extensions,
        accept_multiple_files=True,
        help="Memory-only processing"
    )
    
    if uploaded_files:
        st.info(f"📚 {len(uploaded_files)} file(s) selected")
        
        total_size = 0
        for file in uploaded_files:
            file_size = file.size / 1024
            total_size += file_size
            ext = file.name.split('.')[-1].lower()
            icon = FORMAT_ICONS.get(ext, '🔎')
            st.caption(f"{icon} {file.name} ({file_size:.1f} KB)")
        
        st.caption(f"**Total: {total_size:.1f} KB**")
        
        if st.button("🚀 Process All Files", type="primary"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                status_text.text("Initializing RAG Engine...")
                progress_bar.progress(0.1)
                
                if not st.session_state.rag_engine:
                    st.session_state.rag_engine = RAGEngine(model=selected_model)
                    st.session_state.current_model = selected_model
                
                status_text.text("Processing files...")
                progress_bar.progress(0.2)
                
                all_chunks = []
                for idx, uploaded_file in enumerate(uploaded_files):
                    file_name = uploaded_file.name
                    status_text.text(f"Processing {file_name}... ({idx+1}/{len(uploaded_files)})")
                    progress_bar.progress(0.2 + (idx + 1) / len(uploaded_files) * 0.5)
                    
                    try:
                        chunks = st.session_state.rag_engine.process_uploaded_file(uploaded_file)
                        all_chunks.extend(chunks)
                    except Exception as e:
                        st.warning(f"⚠️ {file_name}: {str(e)}")
                        continue
                
                if not all_chunks:
                    st.error("❌ No content extracted")
                    progress_bar.empty()
                    status_text.empty()
                    st.stop()
                
                status_text.text("Creating vectorstore...")
                progress_bar.progress(0.75)
                st.session_state.rag_engine.create_vectorstore(all_chunks)
                
                status_text.text("Setting up AI chain...")
                progress_bar.progress(0.9)
                st.session_state.rag_engine.setup_chain()
                
                progress_bar.progress(1.0)
                status_text.text("✅ Complete!")
                
                st.session_state.document_processed = True
                st.session_state.processed_files = [f.name for f in uploaded_files]
                
                st.success(f"✅ Processed {len(uploaded_files)} file(s)!")
                st.info(f"📊 {len(all_chunks)} chunks | 🤖 {selected_model}")
                
                time.sleep(1)
                st.rerun()
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                progress_bar.empty()
                status_text.empty()
    
    st.markdown("---")
    
    st.header("📊 System Status")
    
    if st.session_state.rag_engine:
        st.success("🟢 Online")
        st.info(f"🤖 {st.session_state.current_model}")
        
        if st.session_state.document_processed:
            st.success(f"🟢 Files: {len(st.session_state.processed_files)}")
            with st.expander("🔍 View files"):
                for file in st.session_state.processed_files:
                    ext = file.split('.')[-1].lower()
                    icon = FORMAT_ICONS.get(ext, '🔎')
                    st.caption(f"{icon} {file}")
        else:
            st.warning("🟡 No files")
        
        st.info(f"💬 {len(st.session_state.chat_history)} messages")
    else:
        st.error("🔴 Offline")
    
    if st.session_state.document_processed:
        st.markdown("---")
        if st.button("🔄 Reset", type="secondary"):
            st.session_state.chat_history = []
            st.session_state.document_processed = False
            st.session_state.processed_files = []
            if st.session_state.rag_engine:
                st.session_state.rag_engine.clear_documents()
                st.session_state.rag_engine = None
            st.rerun()

if not st.session_state.document_processed:
    st.info("👈 Upload files to start")
    
    with st.expander("📖 Quick Guide"):
        st.markdown("""
        ### How to use:
        
        1. **Select Model** - Choose from your downloaded models
        2. **Upload Files** - PDF, DOCX, CSV, etc.
        3. **Process** - Click "🚀 Process All Files"
        4. **Chat** - Ask questions
        5. **Switch Models** - Change anytime without reprocessing
        
        ### 🌟 Your Available Models:
        
        **Qwen Family (7 models)**
        - Qwen 3 (latest), Qwen 2.5 (stable + 3b variant)
        - Specialized coders included
        
        **DeepSeek (2 models)**
        - Advanced reasoning capabilities
        
        **Llama (2 models)**
        - Meta's latest: 3.2, 3.1
        
        **Mistral (1 model)**
        - Fast & powerful
        
        **Gemma (2 models)**
        - Google's Gemma 3 & 2
        
        **Phi (3 models)**
        - Microsoft's efficient models
        
        **GPT-OSS (2 models)**
        - OpenAI-style open source models
        
        ### Features:
        - ✅ 100% Local (No internet after download)
        - ✅ 100% Free (No API costs)
        - ✅ 100% Private (Data never leaves PC)
        - ✅ 19 AI models ready to use
        - ✅ Instant model switching
        - ✅ Memory-only file processing
        - ✅ Multi-format support
        """)
else:
    st.info(f"🤖 **{st.session_state.current_model}** | {len(st.session_state.processed_files)} file(s) | 💾 Local")
    
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if message["role"] == "assistant" and "sources" in message:
                with st.expander("📚 Sources"):
                    for idx, source in enumerate(message["sources"], 1):
                        source_file = source.metadata.get('source', 'Unknown')
                        source_page = source.metadata.get('page', 'N/A')
                        file_ext = source_file.split('.')[-1].lower() if '.' in source_file else ''
                        icon = FORMAT_ICONS.get(file_ext, '🔎')
                        st.caption(f"**{idx}.** {icon} {source_file} (Page: {source_page})")
                        st.caption(f"_{source.page_content[:200]}..._")
    
    if prompt := st.chat_input("Ask about your files..."):
        st.session_state.chat_history.append({
            "role": "user",
            "content": prompt
        })
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner(f"🤔 {st.session_state.current_model} thinking..."):
                try:
                    response = st.session_state.rag_engine.ask_question(prompt)
                    
                    st.markdown(response["answer"])
                    
                    sources = response.get("source_documents", [])
                    if sources:
                        with st.expander("📚 Sources"):
                            for idx, source in enumerate(sources, 1):
                                source_file = source.metadata.get('source', 'Unknown')
                                source_page = source.metadata.get('page', 'N/A')
                                file_ext = source_file.split('.')[-1].lower() if '.' in source_file else ''
                                icon = FORMAT_ICONS.get(file_ext, '🔎')
                                st.caption(f"**{idx}.** {icon} {source_file} (Page: {source_page})")
                                st.caption(f"_{source.page_content[:200]}..._")
                    
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": response["answer"],
                        "sources": sources
                    })
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")

st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("🚀 TTZ.KT AI - Ollama 2025")
with col2:
    st.caption(f"🤖 {st.session_state.current_model if st.session_state.rag_engine else 'No model'}")
with col3:
    st.caption("v8.0 FINAL - 19 Models")