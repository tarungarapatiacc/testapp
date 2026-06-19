from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# Question Schemas
class QuestionCreate(BaseModel):
    """Schema for creating a question."""
    title: str
    description: str
    category: str
    difficulty: str  # beginner, intermediate, advanced
    context: Optional[str] = None

class QuestionResponse(BaseModel):
    """Schema for question response."""
    id: int
    title: str
    description: str
    category: str
    difficulty: str
    
    class Config:
        from_attributes = True

# Assessment Schemas
class UserResponseCreate(BaseModel):
    """Schema for user response to a question."""
    question_id: int
    response_text: str

class AssessmentResult(BaseModel):
    """Schema for assessment results."""
    human_score: float
    ai_comparison_score: float
    creativity_index: float
    nuance_score: float
    out_of_box_thinking_score: float
    feedback: str
    timestamp: datetime

# User Schemas
class UserCreate(BaseModel):
    """Schema for creating a user."""
    email: str
    username: str
    password: str

class UserLogin(BaseModel):
    """Schema for user login."""
    email: str
    password: str

class TokenResponse(BaseModel):
    """Schema for token response."""
    access_token: str
    token_type: str
