from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.search import router as search_router
from backend.upload import router as upload_router
from backend.image_service import router as image_router



app=FastAPI(
    title="ARIES Astronomical Image Archive",
    description="API for archival and retrieval of astronomical images",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search_router)
app.include_router(upload_router)
app.include_router(image_router)


@app.get("/")
def home():
    return {"message": "ARIES Astronomical Image Archive API is running"}