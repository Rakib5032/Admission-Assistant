from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from app.model.models import embeddings
import os
import shutil

def update_rag():
    pdf_path = "app/data/rag.pdf"
    vector_path = "app/data/faiss_index"
    
    if not os.path.exists(pdf_path):
        raise Exception("Rag.pdf not found")
    
    if os.path.exists(vector_path):
        shutil.rmtree(vector_path)
    
    loader = PyMuPDFLoader(pdf_path)
    
    pages = loader.load()
    
    print("Creating Embeddings...")
    
    db = FAISS.from_documents(
        pages,
        embeddings
    )
    
    db.save_local(vector_path)
    
    # print("RAG updated Successfully..")
    
    return os.path.exists(vector_path)