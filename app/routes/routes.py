from fastapi import APIRouter
from pydantic import BaseModel
from app.service.common_query import common_query
from app.service.chat_service import question_answer
from app.rag.ingest import update_rag

router = APIRouter()

class Query(BaseModel):
    query: str

@router.post("/ask")
async def ask(data: Query):
    
    query = data.query.lower().strip()
    
    result = common_query(query)
    
    if result['success']:
        return{
            'success': True,
            'answer': result["answer"]
        }
    response = question_answer(query)
    return response