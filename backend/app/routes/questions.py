from fastapi import APIRouter, Query
from app.services.question_service import QuestionGenerator
from app.models.schemas import QuestionResponse
from typing import List

router = APIRouter(prefix="/api/questions", tags=["questions"])

@router.get("/random", response_model=List[dict])
async def get_random_questions(
    category: str = Query(None, description="Question category"),
    difficulty: str = Query(None, description="Difficulty level"),
    count: int = Query(1, description="Number of questions", ge=1, le=10)
):
    """Get random questions based on filters."""
    return QuestionGenerator.get_random_questions(
        category=category,
        difficulty=difficulty,
        count=count
    )

@router.get("/categories", response_model=List[str])
async def get_categories():
    """Get available question categories."""
    return list(QuestionGenerator.QUESTION_BANK.keys())

@router.get("/by-category/{category}", response_model=List[dict])
async def get_questions_by_category(category: str):
    """Get all questions for a specific category."""
    return QuestionGenerator.get_questions_by_category(category)
