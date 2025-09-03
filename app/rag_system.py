import torch
import gc
from transformers import pipeline
from langchain_community.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from app.config import Config



class BankingRAGSystem:
    def __init__(self):
        self.llm = None
        self.retriever = None
        self.rag_chain = None
        self._initialize_system()
    
    def _initialize_system(self):
        """Initialize the RAG system components"""
        print("Initializing Banking RAG System...")
        
        # Clear cache
        torch.cuda.empty_cache()
        gc.collect()
        

        # Load and process documents
        print("Loading documents...")
        loader = CSVLoader(file_path=Config.DATA_PATH, source_column='question')
        documents = loader.load()
        
        # Split documents
        print("Splitting documents...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE, 
            chunk_overlap=Config.CHUNK_OVERLAP
        )
        docs = text_splitter.split_documents(documents)
        print(f"Processed {len(docs)} document chunks")
        
        # Create embeddings and vector store
        print("Creating embeddings...")
        embeddings = HuggingFaceEmbeddings(model_name=Config.EMBEDDING_MODEL)
        
        # Use persistent storage for Chroma
        vectorstore = Chroma.from_documents(
            documents=docs, 
            embedding=embeddings,
            persist_directory=Config.CHROMA_PATH
        )
        self.retriever = vectorstore.as_retriever()
        
        # Initialize LLM with CPU for compatibility
        print("Initializing LLM...")
        pipe = pipeline(
            "text-generation",
            model=Config.MODEL_NAME,
            torch_dtype=torch.float16,
            device_map="auto",
            trust_remote_code=True,
            max_new_tokens=Config.MAX_NEW_TOKENS,
            do_sample=True,
            temperature=Config.TEMPERATURE,
            use_cache=False
        )
        
        self.llm = HuggingFacePipeline(pipeline=pipe)
        
        # Create prompt template
        prompt_template_str = """<|user|>
You are a helpful banking customer service assistant. Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't have enough information. Be concise and professional.

CONTEXT:
{context}

QUESTION:
{question}
<|end|>
<|assistant|>
"""
        
        PROMPT = PromptTemplate(
            template=prompt_template_str, 
            input_variables=["context", "question"]
        )
        
        # Create RAG chain
        print("Creating RAG chain...")
        self.rag_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": PROMPT}
        )
        
        print("✅ Banking RAG System initialized successfully!")
    
    def query(self, question):
        """Query the RAG system with a banking question"""
        try:
            if not self.rag_chain:
                return {"error": "RAG system not initialized"}
            
            response = self.rag_chain.invoke({"query": question})
            return response
        except Exception as e:
            return {"error": f"Error processing query: {str(e)}"}
    
    def get_system_info(self):
        """Get system information"""
        return {
            "model": Config.MODEL_NAME,
            "embedding_model": Config.EMBEDDING_MODEL,
            "status": "Ready" if self.rag_chain else "Not Ready"
        }