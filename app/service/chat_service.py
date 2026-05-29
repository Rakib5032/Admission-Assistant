from app.rag.chain import rag_chain

def question_answer(query):
    
    answer = rag_chain.invoke(query)
    
    return {
        "success": True,
        "answer": answer
    }