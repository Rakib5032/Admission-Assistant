from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.routes.admin import router as admin_router
from app.routes.routes import router as chat_router


app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

app.include_router(
    admin_router
)

app.include_router(
    chat_router,
)

@app.get('/')
async def home():
    return FileResponse(
        'app/template/index.html'
    )
    
@app.get("/admin")
async def admin():
       return FileResponse(
           "app/template/admin.html"
       ) 
