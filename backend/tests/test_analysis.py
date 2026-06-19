import pytest
from app.services.analysis_service import ResponseAnalyzer


def test_analyze_response():
    """Test response analysis."""
    response = "I think we should first understand the customer's needs. However, we must also consider the competitive landscape. Perhaps we could offer them an exclusive partnership instead of just trying to win them back."
    
    result = ResponseAnalyzer.analyze_response(response)
    
    assert "human_score" in result
    assert "ai_comparison_score" in result
    assert "creativity_index" in result
    assert "nuance_score" in result
    assert "out_of_box_thinking_score" in result
    assert "feedback" in result
    
    # All scores should be between 0 and 100
    for score in ["human_score", "ai_comparison_score", "creativity_index", "nuance_score", "out_of_box_thinking_score"]:
        assert 0 <= result[score] <= 100


def test_human_score_calculation():
    """Test human score calculation."""
    # Response with personal references
    response = "In my experience, I would feel that this situation requires my personal attention. I believe strongly in this approach."
    
    score = ResponseAnalyzer._calculate_human_score(response)
    assert score > 50  # Should have good human score


def test_creativity_calculation():
    """Test creativity calculation."""
    # Creative response
    response = "What if we reverse our approach? Instead of viewing this as a loss, what if this customer could become a partner or advocate? We could explore hybrid models."
    
    score = ResponseAnalyzer._calculate_creativity(response)
    assert score > 50  # Should have decent creativity score


def test_nuance_calculation():
    """Test nuance score calculation."""
    # Nuanced response with balance
    response = "While it's tempting to immediately try to win them back, we should first understand if the issue is with us or if it's a strategic move for them. However, if there's an opportunity, we should explore it. It depends on their specific needs."
    
    score = ResponseAnalyzer._calculate_nuance(response)
    assert score > 50  # Should have good nuance score
