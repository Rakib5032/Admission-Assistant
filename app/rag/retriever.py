from langchain_community.vectorstores import FAISS
from app.model.models import embeddings

def retriever(query):
    db = FAISS.load_local(
        "app/data/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )
    
    docs = db.similarity_search(
        query,
        k = 1
    )
    return docs