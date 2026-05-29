from langchain_community.vectorstores import FAISS
from app.model.models import embeddings

def load_vector_store():
    
    return FAISS.load_local(
        "app/data/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )