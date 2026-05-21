from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

from app.routes.chat import(
    router as chat_router
)

app.include_router(
    chat_router
)

@app.get('/')
async def home():
    return FileResponse(
        'app/template/index.html'
    )
    
# @app.post('/askk')
# def d(data: dict):
#     return {
#         'success': True,
#         'answer': 'Inside askk'
#     }
