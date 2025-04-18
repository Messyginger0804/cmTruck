from fastapi import APIRouter
from app.config import settings

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"status": "ok"}

@router.get("/version")
async def get_version():
    return {
        "api_version": settings.API_VERSION,
        "yolo_model": settings.YOLO_MODEL_VERSION,
        "llm_model": settings.LLM_MODEL_VERSION,
    }
