# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: LearnPath
import json, base64, zlib

def load_initial_data(json_string: str) -> dict:
    """Deserializes a JSON string containing learning path data and decompresses payloads if needed."""
    try:
        raw = json.loads(json_string)
        for key in ("lessons", "exercises", "milestones"):
            payload = raw.get(key, [])
            if isinstance(payload, list):
                raw[key] = [json.loads(item) if item.startswith("data:") else item for item in payload]
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {e}") from e
    return raw

def compress_payload(data: dict) -> str:
    """Compresses a dictionary into a base64-encoded string prefixed with 'data:' for storage."""
    compressed = zlib.compress(json.dumps(data).encode(), level=9)
    encoded = base64.b64encode(compressed).decode()
    return f"data:{encoded}"

def create_sample_json_string(lessons: list, exercises: list, milestones: list) -> str:
    """Generates a JSON string with compressed payloads for lessons, exercises, and milestones."""
    payload = {
        "lessons": [compress_payload(l) if isinstance(l, dict) else l for l in lessons],
        "exercises": [compress_payload(e) if isinstance(e, dict) else e for e in exercises],
        "milestones": [compress_payload(m) if isinstance(m, dict) else m for m in milestones]
    }
    return json.dumps(payload, indent=2)

# Пример использования: генерация строки и загрузка данных
sample_json = create_sample_json_string(
    lessons=[{"id": 1, "title": "Введение", "duration": 30}],
    exercises=[{"id": 1, "type": "quiz", "questions": ["Что такое Python?"], "answers": ["Язык программирования"]}],
    milestones=[{"id": 1, "name": "Первый шаг", "progress": 0}]
)

initial_data = load_initial_data(sample_json)
