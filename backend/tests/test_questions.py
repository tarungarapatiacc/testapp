import pytest
from app.services.question_service import QuestionGenerator


def test_get_random_questions():
    """Test getting random questions."""
    questions = QuestionGenerator.get_random_questions(count=1)
    
    assert len(questions) == 1
    assert "title" in questions[0]
    assert "description" in questions[0]
    assert "category" in questions[0]
    assert "difficulty" in questions[0]


def test_get_random_questions_by_category():
    """Test getting random questions filtered by category."""
    questions = QuestionGenerator.get_random_questions(category="business", count=1)
    
    assert len(questions) == 1
    assert questions[0]["category"] == "business"


def test_get_questions_by_category():
    """Test getting all questions for a category."""
    questions = QuestionGenerator.get_questions_by_category("business")
    
    assert len(questions) > 0
    assert all(q["category"] == "business" for q in questions)


def test_get_categories():
    """Test getting all available categories."""
    categories = list(QuestionGenerator.QUESTION_BANK.keys())
    
    assert "business" in categories
    assert "technical" in categories
    assert "creative" in categories
