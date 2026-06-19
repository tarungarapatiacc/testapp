from fastapi import APIRouter, HTTPException
from app.models.schemas import UserResponseCreate, AssessmentResult
from app.services.analysis_service import ResponseAnalyzer
from datetime import datetime

router = APIRouter(prefix="/api/assessment", tags=["assessment"])

@router.post("/analyze", response_model=dict)
async def analyze_response(user_response: UserResponseCreate):
    """Analyze a user's response to a question."""
    
    if not user_response.response_text.strip():
        raise HTTPException(status_code=400, detail="Response cannot be empty")
    
    # Analyze the response
    analysis = ResponseAnalyzer.analyze_response(user_response.response_text)
    
    # Add metadata
    analysis["timestamp"] = datetime.now().isoformat()
    analysis["question_id"] = user_response.question_id
    
    return analysis
