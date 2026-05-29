from fastapi import APIRouter, UploadFile, File
import shutil
import os
from app.rag.update_rag import update_rag
from fastapi.responses import FileResponse

router = APIRouter(
    prefix="/admin"
)

@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)):
    
    save_path= "app/data/rag.pdf"
    
    if os.path.exists(save_path):
        os.remove(save_path)
        
    with open(
        save_path,
        "wb"
    ) as buffer:
        
        shutil.copyfileobj(
            file.file,
            buffer
        )
        
    return{
        'success': True,
        'message': "Uploaded",
    }

@router.post('/update-rag')
async def update():
    update_rag()
    return {
        'success': True,
        'message': 'Rag updated Successfully'
    }

@router.get("/seePDF")
async def see_pdf():
    pdf_path = "app/data/rag.pdf"
    
    if not os.path.exists(pdf_path):
        return {
            # 'success': False,
            # 'message': 'No pdf found'
            'No PDF Exist'
        }

    return FileResponse(
        pdf_path,
        media_type="application/pdf"
    )