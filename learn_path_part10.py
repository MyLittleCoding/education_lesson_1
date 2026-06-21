# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: LearnPath
def export_state_to_json():
    import json
    state = {
        "lessons": [
            {"id": 1, "title": "Введение", "status": "completed"},
            {"id": 2, "title": "Переменные", "status": "in_progress"}
        ],
        "practice_tasks": [
            {"id": 101, "lesson_id": 1, "status": "done"},
            {"id": 102, "lesson_id": 2, "status": "pending"}
        ],
        "milestones": [
            {"title": "Первый шаг", "completed_at": "2023-10-27T10:00:00Z"},
            {"title": "Основы синтаксиса", "completed_at": None}
        ],
        "progress_percent": 45.5,
        "last_updated": "2023-10-27T12:30:00Z"
    }
    return json.dumps(state, indent=2)
