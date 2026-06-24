# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: LearnPath
import json, os

def load_learning_data(filepath: str) -> dict | None:
    if not os.path.exists(filepath):
        print(f"Файл {filepath} не найден.")
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать корневой объект")
        print(f"Данные успешно загружены из {filepath}")
        return data
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {filepath}: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке файла {filepath}: {type(e).__name__}")
        return None

if __name__ == "__main__":
    data = load_learning_data("learning_path.json")
    if data:
        for key, value in data.items():
            print(f"{key}: {value}")
