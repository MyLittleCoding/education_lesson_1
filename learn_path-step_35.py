# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: LearnPath
def get_next_action(current_status, user_input):
    """Returns a recommendation based on the learner's current progress."""
    if not current_status:
        return "Start with Lesson 1."
    
    has_lessons = any(c.get("status") == "complete" for c in current_status.values() if isinstance(c, dict))
    has_practice = any(c.get("type") == "practice" and c.get("status") == "completed" for c in current_status.values())
    has_milestone = any(c.get("type") == "milestone" and c.get("status") == "passed" for c in current_status.values())

    if not has_lessons:
        return "Begin with the first lesson to build your foundation."
    
    if not has_practice:
        return "Now that you've completed some lessons, try a practice exercise to reinforce what you learned."
    
    if not has_milestone:
        return "Great progress! Take a milestone assessment to check how well you've retained the material so far."
    
    return "You've hit all major checkpoints. Review your weak areas and continue advancing through new lessons!"
