# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: LearnPath
import json
from datetime import datetime, timedelta

# Демонстрационные данные: уроки и прогресс пользователя
LESSONS = [
    {"id": 1, "title": "Введение в Python", "status": "completed"},
    {"id": 2, "title": "Переменные и типы", "status": "in_progress"},
    {"id": 3, "title": "Условия и циклы", "status": "pending"}
]

# Текущее состояние приложения (имитация базы данных)
APP_STATE = {
    "last_login": datetime.now().isoformat(),
    "current_lesson_id": 2,
    "completed_count": 1,
    "user_name": "Олег"
}

def save_state():
    """Сохраняет состояние приложения в файл."""
    with open("learnpath_data.json", "w", encoding="utf-8") as f:
        json.dump(APP_STATE, f, ensure_ascii=False)

def load_state():
    """Загружает состояние приложения из файла."""
    try:
        with open("learnpath_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return APP_STATE.copy()

# Инициализация состояния при запуске
if __name__ == "__main__":
    state = load_state()
    print(f"Добро пожаловать, {state['user_name']}!")
    print(f"Текущий урок: {LESSONS[state['current_lesson_id'] - 1]['title']}")
    save_state()
