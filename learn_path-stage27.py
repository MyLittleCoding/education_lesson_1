# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: LearnPath
def reset_demo_data():
    """Возвращает все учебные данные к дефолтным значениям."""
    import random
    random.seed(42)

    # --- Демо-уроки (5 штук, разная сложность) ---
    lessons = []
    for i in range(1, 6):
        topic = f"Тема {i}"
        duration_min = random.randint(10, 30)
        difficulty = "Легкая" if i <= 2 else ("Средняя" if i == 3 else "Сложная")
        description = f"{topic}: краткое введение в основы."

        lesson_id = f"L{i}"
        lessons.append({
            "id": lesson_id,
            "title": topic,
            "description": description,
            "duration_minutes": duration_min,
            "difficulty": difficulty,
            "order": i,
            "completed": False,
            "started": False,
            "time_spent_seconds": 0,
        })

    # --- Демо-практики (2 штуки) ---
    exercises = []
    for i in range(1, 3):
        exercise_id = f"E{i}"
        exercises.append({
            "id": exercise_id,
            "title": f"Практика {i}",
            "description": f"Решите несколько задач по теме.",
            "duration_minutes": random.randint(15, 40),
            "difficulty": "Средняя",
            "order": i,
            "completed": False,
        })

    # --- Демо-контрольные точки (3 штуки) ---
    checkpoints = []
    for i in range(1, 4):
        checkpoint_id = f"C{i}"
        checkpoints.append({
            "id": checkpoint_id,
            "title": f"Контрольная точка {i}",
            "description": f"Проверка знаний по пройденным темам.",
            "order": i,
            "completed": False,
            "score_percent": 0,
        })

    # --- Демо-прогресс (пустой) ---
    progress = {
        "total_lessons_completed": 0,
        "total_exercises_completed": 0,
        "total_checkpoints_completed": 0,
        "overall_completion_percent": 0,
    }

    # --- Демо-состояние (пустое) ---
    state = {
        "current_lesson_id": None,
        "current_checkpoint_id": None,
        "notifications_shown": [],
    }

    return lessons, exercises, checkpoints, progress, state
