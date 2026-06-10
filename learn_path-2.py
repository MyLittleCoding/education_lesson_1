# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: LearnPath
class ValidationError(Exception):
    pass

def validate_user_input(data: dict) -> dict:
    errors = []
    if not isinstance(data, dict):
        raise ValidationError("Ввод должен быть словарем.")
    if "lesson_id" in data and (not isinstance(data["lesson_id"], int) or data["lesson_id"] <= 0):
        errors.append("lesson_id должен быть положительным целым числом.")
    if "user_name" in data and not isinstance(data["user_name"], str):
        errors.append("user_name должен быть строкой.")
    if "progress" in data:
        if not isinstance(data["progress"], (int, float)) or not (0 <= data["progress"] <= 100):
            errors.append("progress должен быть числом от 0 до 100.")
    if errors:
        raise ValidationError("; ".join(errors))
    return data
