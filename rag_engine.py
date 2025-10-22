import os
import time
import tempfile
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
    CSVLoader,
    UnstructuredExcelLoader,
    JSONLoader,
    UnstructuredXMLLoader,
    UnstructuredRTFLoader
)

try:
    from langchain_community.document_loaders import UnstructuredImageLoader
    IMAGE_SUPPORT = True
except ImportError:
    IMAGE_SUPPORT = False


class RAGEngine:
    """
    Multi-Format RAG Engine - FIXED RETRIEVAL
    - Better chunking to keep questions together
    - More chunks retrieved
    - Better prompting
    """
    
    def __init__(self, model="qwen2.5:7b"):
        print(f"[RAG] Initializing with {model}")
        self.model = model
        self.vectorstore = None
        self.chain = None
        self.llm = None
        self.memory = None
        self.processed_documents = []
        
        print("[RAG] Loading embeddings...")
        import torch
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f"[RAG] Using device: {device.upper()}")
        
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': device},
            encode_kwargs={'normalize_embeddings': True, 'batch_size': 32}
        )
        
        self.vector_dir = os.path.join("vectors", "faiss_index")
        if os.path.exists(self.vector_dir):
            try:
                print("[RAG] Loading existing vectorstore...")
                self.vectorstore = FAISS.load_local(
                    self.vector_dir, 
                    self.embeddings, 
                    allow_dangerous_deserialization=True
                )
                print(f"[RAG] Loaded saved vectors ✅")
            except Exception as e:
                print(f"[RAG] Could not load vectors: {e}")
        
        print("[RAG] Ready!")
    
    def _detect_file_type(self, file_name):
        return os.path.splitext(file_name)[1].lower().lstrip('.')
    
    def _load_document_by_type(self, file_path):
        file_type = self._detect_file_type(file_path)
        file_name = os.path.basename(file_path)
        
        try:
            if file_type == 'pdf':
                return PyPDFLoader(file_path).load()
            elif file_type in ['docx', 'doc']:
                return Docx2txtLoader(file_path).load()
            elif file_type in ['txt', 'md']:
                return TextLoader(file_path, encoding='utf-8').load()
            elif file_type == 'rtf':
                return UnstructuredRTFLoader(file_path).load()
            elif file_type == 'csv':
                return CSVLoader(file_path, encoding='utf-8').load()
            elif file_type in ['xlsx', 'xls', 'ods']:
                return UnstructuredExcelLoader(file_path, mode="elements").load()
            elif file_type == 'json':
                return JSONLoader(file_path=file_path, jq_schema='.', text_content=False).load()
            elif file_type == 'xml':
                return UnstructuredXMLLoader(file_path).load()
            elif file_type in ['yaml', 'yml']:
                return TextLoader(file_path, encoding='utf-8').load()
            elif file_type in ['png', 'jpg', 'jpeg', 'bmp', 'tiff', 'gif']:
                if IMAGE_SUPPORT:
                    return UnstructuredImageLoader(file_path).load()
                else:
                    from langchain.schema import Document
                    return [Document(page_content=f"[Image: {file_name}]", metadata={"source": file_name})]
            else:
                from langchain.schema import Document
                return [Document(page_content=f"[Unsupported: {file_type}]", metadata={"source": file_name})]
        except Exception as e:
            print(f"[RAG] Error loading {file_name}: {e}")
            from langchain.schema import Document
            return [Document(page_content=f"[Error: {file_name}]", metadata={"source": file_name})]
    
    def process_uploaded_file(self, uploaded_file):
        """Process uploaded file - BETTER CHUNKING"""
        file_name = uploaded_file.name
        file_type = self._detect_file_type(file_name)
        
        tmp_path = None
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_type}") as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_path = tmp_file.name
            
            documents = self._load_document_by_type(tmp_path)
            
            if tmp_path and os.path.exists(tmp_path):
                os.unlink(tmp_path)
            
            if not documents:
                return []
            
            # FIXED: Larger chunks with more overlap to keep questions together
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1200,  # Larger chunks to keep related content together
                chunk_overlap=300,  # More overlap to prevent splitting questions
                separators=["\n\n\n", "\n\n", "\n", ". ", " ", ""],
                length_function=len
            )
            
            chunks = text_splitter.split_documents(documents)
            
            for chunk in chunks:
                chunk.metadata['source'] = file_name
            
            self.processed_documents.append(file_name)
            print(f"[RAG] {file_name}: {len(chunks)} chunks (larger size for better context)")
            return chunks
            
        except Exception as e:
            if tmp_path and os.path.exists(tmp_path):
                os.unlink(tmp_path)
            print(f"[RAG] Error processing {file_name}: {e}")
            raise
    
    def create_vectorstore(self, chunks):
        """Create FAISS vectorstore"""
        print(f"[RAG] Creating vectorstore from {len(chunks)} chunks...")
        start_time = time.time()
        
        if not chunks:
            raise ValueError("No chunks provided")
        
        self.vectorstore = FAISS.from_documents(chunks, embedding=self.embeddings)
        
        elapsed = time.time() - start_time
        print(f"[RAG] Vectorstore created in {elapsed:.2f}s")
        
        os.makedirs(self.vector_dir, exist_ok=True)
        try:
            self.vectorstore.save_local(self.vector_dir)
            print(f"[RAG] Vectorstore saved ✅")
        except Exception as e:
            print(f"[RAG] Could not save vectorstore: {e}")
    
    def setup_chain(self):
        """Setup chain - MORE CHUNKS RETRIEVED"""
        if not self.vectorstore:
            raise ValueError("Vectorstore not initialized")
        
        print(f"[RAG] Setting up chain with {self.model}...")
        
        # Faster settings for qwen2.5:7b
        self.llm = ChatOllama(
            model=self.model,
            temperature=0.2,
            num_predict=256,      # ← Reduce from 512 to 256
            num_ctx=2048,         # ← Reduce from 4096 to 2048
            timeout=120,
            keep_alive="10m",
            num_gpu=1             # ← Add this line
        )
        
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )
        
        # FIXED: Better prompt that asks to use ALL context
        qa_prompt = PromptTemplate(
            template="""You are answering questions based on provided document context. Use ALL the context below to give a complete answer.

Context from documents:
{context}

Question: {question}

Instructions:
- Read through ALL the context carefully
- If listing items (like questions), list ALL of them that appear in the context
- If information is incomplete, say so
- Answer based ONLY on the context above

Answer:""",
            input_variables=["context", "question"]
        )
        
        # FIXED: Retrieve MORE chunks to get complete information
        self.chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(
                search_type="similarity",  # Simple similarity works better for lists
                search_kwargs={
                    "k": 6  # Get 6 chunks instead of 3 (more complete info)
                }
            ),
            memory=self.memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={"prompt": qa_prompt},
            verbose=False
        )
        
        print(f"[RAG] Chain ready with 6-chunk retrieval ✅")
    
    def switch_model(self, new_model):
        """Switch model"""
        if not self.vectorstore:
            raise ValueError("No documents processed")
        
        print(f"[RAG] Switching to {new_model}...")
        
        self.llm = ChatOllama(
            model=new_model,
            temperature=0.2,
            num_predict=512,
            num_ctx=4096,
            timeout=120,
            keep_alive="10m"
        )
        
        qa_prompt = PromptTemplate(
            template="""You are answering questions based on provided document context. Use ALL the context below to give a complete answer.

Context from documents:
{context}

Question: {question}

Instructions:
- Read through ALL the context carefully
- If listing items (like questions), list ALL of them that appear in the context
- If information is incomplete, say so
- Answer based ONLY on the context above

Answer:""",
            input_variables=["context", "question"]
        )
        
        self.chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 6}
            ),
            memory=self.memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={"prompt": qa_prompt},
            verbose=False
        )
        
        self.model = new_model
        print(f"[RAG] Switched to {new_model} ✅")
    
    def ask_question(self, question):
        """Ask question with timing and debug info"""
        if not self.chain:
            raise ValueError("Chain not initialized")
        
        print(f"\n{'='*60}")
        print(f"[QUERY] {question}")
        print(f"{'='*60}")
        
        total_start = time.time()
        
        try:
            response = self.chain.invoke({"question": question})
            
            total_time = time.time() - total_start
            
            sources = response.get("source_documents", [])
            print(f"\n[INFO] Retrieved {len(sources)} chunks in {total_time:.2f}s")
            print(f"[INFO] Total response time: {total_time:.2f}s")
            
            # Show what was retrieved (for debugging)
            for i, doc in enumerate(sources, 1):
                preview = doc.page_content[:150].replace('\n', ' ')
                print(f"  Chunk {i}: {preview}...")
            
            print(f"{'='*60}\n")
            
            return {
                "answer": response["answer"],
                "source_documents": sources
            }
            
        except Exception as e:
            print(f"[ERROR] Query failed: {e}")
            import traceback
            traceback.print_exc()
            raise
    
    def clear_documents(self):
        """Clear all"""
        self.vectorstore = None
        self.chain = None
        self.llm = None
        self.memory = None
        self.processed_documents = []
        
        # Also clear saved vectors to force reprocessing with new settings
        if os.path.exists(self.vector_dir):
            import shutil
            shutil.rmtree(self.vector_dir)
            print("[RAG] Cleared vectors directory")
        
        print("[RAG] Cleared completely")