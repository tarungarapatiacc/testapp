"""Service for analyzing responses and generating scores."""

from typing import Dict, Any
import re

class ResponseAnalyzer:
    """Analyze user responses for nuance, creativity, and out-of-box thinking."""
    
    @staticmethod
    def analyze_response(response_text: str, question_context: str = "") -> Dict[str, Any]:
        """Analyze a user response and generate scores."""
        
        scores = {
            "human_score": ResponseAnalyzer._calculate_human_score(response_text),
            "ai_comparison_score": ResponseAnalyzer._calculate_ai_comparison_score(response_text),
            "creativity_index": ResponseAnalyzer._calculate_creativity(response_text),
            "nuance_score": ResponseAnalyzer._calculate_nuance(response_text),
            "out_of_box_thinking_score": ResponseAnalyzer._calculate_out_of_box_thinking(response_text),
        }
        
        # Generate feedback
        feedback = ResponseAnalyzer._generate_feedback(scores, response_text)
        scores["feedback"] = feedback
        
        return scores
    
    @staticmethod
    def _calculate_human_score(response_text: str) -> float:
        """Calculate human-like thinking score (0-100)."""
        # Factors: Personal experience, emotion, subjectivity
        score = 0
        
        # Check for personal references
        personal_keywords = ["I", "me", "my", "experience", "feel", "believe"]
        personal_count = sum(response_text.lower().count(kw) for kw in personal_keywords)
        score += min(personal_count * 5, 30)
        
        # Check for contextual awareness
        if len(response_text.split()) > 30:  # Longer, more thoughtful responses
            score += 20
        
        # Check for nuanced language
        nuanced_words = ["however", "although", "while", "perhaps", "consider", "might"]
        nuanced_count = sum(response_text.lower().count(kw) for kw in nuanced_words)
        score += min(nuanced_count * 10, 30)
        
        # Check for questions (curiosity)
        if "?" in response_text:
            score += 20
        
        return min(score, 100)
    
    @staticmethod
    def _calculate_ai_comparison_score(response_text: str) -> float:
        """Calculate how different from algorithmic thinking (0-100)."""
        # Factors: Emotion, subjectivity, uncertainty
        score = 0
        
        # Check for emotional language
        emotional_words = ["feel", "love", "hate", "concerned", "excited", "frustrated"]
        emotional_count = sum(response_text.lower().count(kw) for kw in emotional_words)
        score += min(emotional_count * 15, 40)
        
        # Check for uncertainty (human trait)
        uncertainty_words = ["might", "perhaps", "probably", "maybe", "could", "uncertain"]
        uncertainty_count = sum(response_text.lower().count(kw) for kw in uncertainty_words)
        score += min(uncertainty_count * 12, 35)
        
        # Check for domain-specific knowledge
        if len(response_text.split()) > 50:
            score += 25
        
        return min(score, 100)
    
    @staticmethod
    def _calculate_creativity(response_text: str) -> float:
        """Calculate creativity score (0-100)."""
        score = 0
        
        # Unusual word combinations
        words = response_text.lower().split()
        if len(set(words)) / max(len(words), 1) > 0.6:  # High vocabulary diversity
            score += 30
        
        # Novel approaches indicators
        creative_phrases = ["instead of", "what if", "alternative", "unconventional", "unique", "different approach"]
        creative_count = sum(response_text.lower().count(phrase) for phrase in creative_phrases)
        score += min(creative_count * 20, 40)
        
        # Long, thoughtful response
        if len(response_text.split()) > 60:
            score += 30
        
        return min(score, 100)
    
    @staticmethod
    def _calculate_nuance(response_text: str) -> float:
        """Calculate nuance and sophistication score (0-100)."""
        score = 0
        
        # Contradiction or balance
        balance_words = ["however", "but", "although", "on the other hand", "conversely"]
        balance_count = sum(response_text.lower().count(kw) for kw in balance_words)
        score += min(balance_count * 20, 40)
        
        # Conditional thinking
        conditional_words = ["if", "then", "depends", "depending on", "it depends"]
        conditional_count = sum(response_text.lower().count(kw) for kw in conditional_words)
        score += min(conditional_count * 15, 35)
        
        # Qualification and context
        qualification_words = ["specifically", "particularly", "notably", "importantly", "significantly"]
        qualification_count = sum(response_text.lower().count(kw) for kw in qualification_words)
        score += min(qualification_count * 12, 25)
        
        return min(score, 100)
    
    @staticmethod
    def _calculate_out_of_box_thinking(response_text: str) -> float:
        """Calculate out-of-box thinking score (0-100)."""
        score = 0
        
        # Lateral thinking indicators
        lateral_words = ["assumption", "paradox", "contradiction", "perspective", "reframe", "invert"]
        lateral_count = sum(response_text.lower().count(kw) for kw in lateral_words)
        score += min(lateral_count * 18, 35)
        
        # Problem reframing
        reframing_words = ["actually", "rather than", "instead", "reverse", "flip"]
        reframing_count = sum(response_text.lower().count(kw) for kw in reframing_words)
        score += min(reframing_count * 15, 30)
        
        # Creative solutions
        solution_words = ["combine", "hybrid", "blend", "merge", "integrate"]
        solution_count = sum(response_text.lower().count(kw) for kw in solution_words)
        score += min(solution_count * 20, 35)
        
        return min(score, 100)
    
    @staticmethod
    def _generate_feedback(scores: Dict[str, float], response_text: str) -> str:
        """Generate personalized feedback based on scores."""
        feedback = []
        
        if scores["out_of_box_thinking_score"] > 70:
            feedback.append("✨ Excellent out-of-box thinking! You challenge conventional approaches.")
        elif scores["out_of_box_thinking_score"] > 50:
            feedback.append("📌 Good creative thinking. Consider exploring more unconventional perspectives.")
        else:
            feedback.append("💡 Try to think more laterally. Challenge your initial assumptions.")
        
        if scores["nuance_score"] > 75:
            feedback.append("🎯 Your response shows sophisticated nuance and context-awareness.")
        elif scores["nuance_score"] > 50:
            feedback.append("⚖️ Add more nuance by considering multiple perspectives and trade-offs.")
        
        if scores["ai_comparison_score"] > 70:
            feedback.append("🧠 Your thinking is distinctly human - rich with context and intuition.")
        else:
            feedback.append("🤖 Consider adding more human elements - emotion, intuition, real-world experience.")
        
        return " ".join(feedback)
