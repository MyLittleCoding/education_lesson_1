# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: LearnPath
import json, os

DATA_FILE = "learnpath_data.json"

def save_state(state):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def load_state():
    if not os.path.exists(DATA_FILE):
        return {"lessons": [], "completed_lessons": set(), "current_step": 0}
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            # Восстанавливаем типы данных (на случай если файл был создан в другой версии)
            if isinstance(data.get("completed_lessons"), list):
                data["completed_lessons"] = set(data["completed_lessons"])
            return data
        except json.JSONDecodeError:
            print(f"Ошибка чтения {DATA_FILE}, создаю новый.")
            return {"lessons": [], "completed_lessons": set(), "current_step": 0}

def add_lesson(lesson_id, title):
    state = load_state()
    if lesson_id not in [l["id"] for l in state["lessons"]]:
        state["lessons"].append({"id": lesson_id, "title": title})
        save_state(state)
        return True
    return False

def mark_completed(lesson_id):
    state = load_state()
    if lesson_id in [l["id"] for l in state["lessons"]]:
        state["completed_lessons"].add(lesson_id)
        # Обновляем текущий шаг, если это не последний урок
        next_step = min([i+1 for i, l in enumerate(state["lessons"]) if l["id"] == lesson_id])
        if next_step < len(state["lessons"]):
            state["current_step"] = next_step
        save_state(state)
        return True
    return False

def get_progress():
    state = load_state()
    total = len(state["lessons"])
    completed = len(state["completed_lessons"].intersection({l["id"] for l in state["lessons"]} if state["lessons"] else set()))
    progress_percent = (completed / total * 100) if total > 0 else 0.0
    return {
        "total": total,
        "completed": completed,
        "current_step": state.get("current_step", 0),
        "progress_percent": round(progress_percent, 2)
    }

# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: LearnPath
import json, os

DATA_FILE = "learnpath_data.json"

def save_state(state):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def load_state():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}
