from fastapi import APIRouter
from pydantic import BaseModel
from uuid import UUID

router = APIRouter()


class FeedbackIn(BaseModel):
    estimate_id: UUID
    feedback: str


@router.post("/feedback/")
async def add_feedback(data: FeedbackIn):
    # Find estimate in DB
    # Add feedback
    return {"message": "Feedback added successfully"}
