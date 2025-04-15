from fastapi import APIRouter, UploadFile, File, Form
from uuid import UUID

router = APIRouter()


@router.get("/ping")
async def ping():
    return {"message": "pong"}


@router.post("/estimate/")
async def create_estimate(
    image: UploadFile = File(...),
    client_name: str = Form(...),
    client_phone: str = Form(...),
):
    # 1. Save image
    # 2. Send to YOLO Pi
    # 3. Get YOLO result
    # 4. Send YOLO + Form to LLM
    # 5. Save all to DB
    # 6. Return Estimate ID + response

    return {"message": "Estimate created"}


@router.get("/estimate/{estimate_id}")
async def get_estimate(estimate_id: UUID):
    # Pull from DB
    return {"message": f"Estimate details for {estimate_id}"}
