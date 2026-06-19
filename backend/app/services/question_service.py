"""Service for question generation and management."""

from typing import List, Dict, Any
import random

class QuestionGenerator:
    """Generate contextual questions for assessment."""
    
    QUESTION_BANK = {
        "business": [
            {
                "title": "Customer Retention Crisis",
                "description": "A loyal customer of 10 years suddenly switches to a competitor. Your company loses them. What would you do?",
                "difficulty": "intermediate",
                "context": "You're a customer success manager"
            },
            {
                "title": "Budget Constraints",
                "description": "You have a brilliant product idea but limited budget. How do you validate it with minimal resources?",
                "difficulty": "advanced",
                "context": "You're a startup founder"
            },
        ],
        "technical": [
            {
                "title": "System Design Challenge",
                "description": "Design a system to handle 1 million concurrent users. What's your approach?",
                "difficulty": "advanced",
                "context": "You're a senior architect"
            },
            {
                "title": "Legacy Code Refactoring",
                "description": "You inherit a 20-year-old monolith. How would you modernize it without breaking production?",
                "difficulty": "advanced",
                "context": "You're a tech lead"
            },
        ],
        "creative": [
            {
                "title": "Product Pivot",
                "description": "Your product failed in market A but succeeded unexpectedly in market B. What insights do you draw?",
                "difficulty": "intermediate",
                "context": "You're a product manager"
            },
            {
                "title": "Think Outside the Box",
                "description": "How would you sell a refrigerator to someone living in the Arctic?",
                "difficulty": "beginner",
                "context": "Sales challenge"
            },
        ]
    }
    
    @staticmethod
    def get_random_questions(category: str = None, difficulty: str = None, count: int = 1) -> List[Dict[str, Any]]:
        """Get random questions based on filters."""
        
        # Get all questions
        all_questions = []
        for cat, questions in QuestionGenerator.QUESTION_BANK.items():
            if category and cat != category:
                continue
            for q in questions:
                if difficulty and q["difficulty"] != difficulty:
                    continue
                all_questions.append({"category": cat, **q})
        
        # Return random selection
        return random.sample(all_questions, min(count, len(all_questions)))
    
    @staticmethod
    def get_questions_by_category(category: str) -> List[Dict[str, Any]]:
        """Get all questions for a category."""
        if category not in QuestionGenerator.QUESTION_BANK:
            return []
        return [{"category": category, **q} for q in QuestionGenerator.QUESTION_BANK[category]]
