#!/usr/bin/env python
"""CLI interface for the assessment agent."""

import sys
from assessor import HumanAIAssessor
from question_generator import DynamicQuestionGenerator
from config import agent_config

def print_header(text: str):
    """Print formatted header."""
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")

def run_cli_assessment():
    """Run interactive CLI assessment."""
    
    print_header("🤖 Human vs AI Thinking Assessment Agent")
    print(f"Agent: {agent_config.AGENT_NAME} v{agent_config.AGENT_VERSION}")
    print()
    
    user_id = input("📝 Enter your user ID (or press Enter for guest): ").strip()
    if not user_id:
        user_id = "guest_" + str(hash("guest"))[:8]
    
    assessor = HumanAIAssessor(user_id)
    
    print("\n📚 Choose a domain:")
    domains = DynamicQuestionGenerator.get_available_domains()
    for i, domain in enumerate(domains, 1):
        print(f"  {i}. {domain.capitalize()}")
    
    domain_choice = input("Enter choice (1-{}, default 1): ".format(len(domains))).strip()
    domain = domains[int(domain_choice) - 1] if domain_choice else domains[0]
    
    print("\n⚙️  Choose difficulty level:")
    difficulties = DynamicQuestionGenerator.get_difficulties()
    for i, diff in enumerate(difficulties, 1):
        print(f"  {i}. {diff.capitalize()}")
    
    difficulty_choice = input("Enter choice (1-{}, default 2): ".format(len(difficulties))).strip()
    difficulty = difficulties[int(difficulty_choice) - 1] if difficulty_choice else difficulties[1]
    
    result = assessor.start_assessment(
        domain=domain,
        difficulty=difficulty,
        questions_count=3
    )
    
    print(result["welcome_message"])
    
    question_num = 1
    total_questions = 3
    
    while question_num <= total_questions:
        print_header(f"Question {question_num} of {total_questions}")
        
        question = assessor.get_next_question()
        print(f"🎯 {question['title']}")
        print(f"📋 {question['question']}")
        if question['context']:
            print(f"📌 Context: {question['context']}")
        
        print()
        print("Your response (press Enter twice when done):")
        print("-" * 40)
        
        lines = []
        while True:
            line = input()
            if not line:
                if lines:
                    break
                continue
            lines.append(line)
        
        response_text = "\n".join(lines)
        
        print("\n⏳ Analyzing your response...\n")
        result = assessor.submit_response(response_text)
        
        if result["status"] == "success":
            analysis = result["analysis"]
            
            print("📊 Your Scores:")
            print(f"  • Human Thinking Index: {analysis['human_score']:.1f}/100")
            print(f"  • AI Comparison Score: {analysis['ai_comparison_score']:.1f}/100")
            print(f"  • Creativity Index: {analysis['creativity_index']:.1f}/100")
            print(f"  • Nuance Score: {analysis['nuance_score']:.1f}/100")
            print(f"  • Out-of-Box Thinking: {analysis['out_of_box_thinking_score']:.1f}/100")
            print(f"\n  Overall: {analysis['overall_score']:.1f}/100")
            
            print(f"\n💡 Feedback: {analysis['feedback']}")
            
            if analysis.get('key_findings'):
                print("\n🔍 Key Findings:")
                for finding in analysis['key_findings']:
                    print(f"  • {finding}")
        
        question_num += 1
        
        if question_num <= total_questions:
            input("\nPress Enter to continue to the next question...")
    
    print_header("Assessment Complete!")
    final_result = assessor.end_assessment()
    
    print(final_result["summary"])
    print("\n✨ Thank you for taking the Human vs AI Thinking Assessment!")
    print(f"Session ID: {final_result['session_id']}")
    print()

if __name__ == "__main__":
    try:
        run_cli_assessment()
    except KeyboardInterrupt:
        print("\n\n👋 Assessment interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
