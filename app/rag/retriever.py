from app.rag.vector_store import load_vector_store

def retriever(query):
    db = load_vector_store()
    
    docs = db.similarity_search(
        query,
        k = 1
    )
    
    return "\n\n".join(
        doc.page_content for doc in docs
    )