from sqlalchemy import Column, Integer, String, DateTime, Float, Text
from datetime import datetime
from .database import Base

class Question(Base):
    """Question model."""
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), unique=True, index=True)
    description = Column(Text)
    category = Column(String(50), index=True)
    difficulty = Column(String(20))
    context = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class UserResponse(Base):
    """User response model."""
    __tablename__ = "user_responses"
    
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, index=True)
    response_text = Column(Text)
    human_score = Column(Float)
    ai_comparison_score = Column(Float)
    creativity_index = Column(Float)
    nuance_score = Column(Float)
    out_of_box_thinking_score = Column(Float)
    overall_score = Column(Float)
    feedback = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
