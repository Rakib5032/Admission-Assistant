from fastapi import APIRouter
from pydantic import BaseModel
from app.routes.common_query import common_query

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
            
    return{
        'success': False,
        'answer': data
    }