# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: LearnPath
def undo_last_action(history):
    """Откатывает последнее действие из истории (кроме 'init' и 'clear')."""
    if not history:
        return None
    last = history[-1]
    if last.get("type") in ("init", "clear"):
        return None  # нельзя отменить системные действия
    action_type, payload = list(last.items())[:2]
    if action_type == "add_lesson":
        lesson_id = payload["id"]
        history.pop()
        lessons.remove(lesson_id)
        undo_stack.append({"type": "remove", "target": f"lesson:{lesson_id}"})
        return {"status": "undone", "action": "add_lesson"}
    elif action_type == "start_practice":
        lesson_id = payload["id"]
        history.pop()
        lessons[lesson_id]["practice_started_at"] = None
        undo_stack.append({"type": "remove", "target": f"practice:{lesson_id}"})
        return {"status": "undone", "action": "start_practice"}
    elif action_type == "end_practice":
        lesson_id = payload["id"]
        history.pop()
        lessons[lesson_id]["practiced_at"] = None
        undo_stack.append({"type": "remove", "target": f"practice:{lesson_id}"})
        return {"status": "undone", "action": "end_practice"}
    elif action_type == "add_quiz":
        quiz_id = payload["id"]
        history.pop()
        quizzes.remove(quiz_id)
        undo_stack.append({"type": "remove", "target": f"quiz:{quiz_id}"})
        return {"status": "undone", "action": "add_quiz"}
    elif action_type == "start_quiz":
        quiz_id = payload["id"]
        history.pop()
        quizzes[quiz_id]["started_at"] = None
        undo_stack.append({"type": "remove", "target": f"quiz:{quiz_id}"})
        return {"status": "undone", "action": "start_quiz"}
    elif action_type == "end_quiz":
        quiz_id = payload["id"]
        history.pop()
        quizzes[quiz_id]["completed_at"] = None
        undo_stack.append({"type": "remove", "target": f"quiz:{quiz_id}"})
        return {"status": "undone", "action": "end_quiz"}
    elif action_type == "add_checkpoint":
        checkpoint_id = payload["id"]
        history.pop()
        checkpoints.remove(checkpoint_id)
        undo_stack.append({"type": "remove", "target": f"checkpoint:{checkpoint_id}"})
        return {"status": "undone", "action": "add_checkpoint"}
    else:
        # для остальных типов просто сбрасываем в состояние до этого действия
        history.pop()
        return {"status": "undone", "action": action_type}
