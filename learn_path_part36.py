# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: LearnPath
def repair_and_verify(data):
    """Проверяет целостность данных и чинит типичные проблемы."""
    issues = []
    if not data:
        return data, ["Данные пустые"]
    
    for i in range(len(data)):
        item = data[i]
        try:
            if isinstance(item, dict):
                keys = list(item.keys())
                if len(keys) != 1 or any(k not in ("topic", "level", "status") for k in keys):
                    issues.append(f"Неверная структура в позиции {i}: {item}")
                    data[i] = {"topic": item.get("topic", ""), "level": item.get("level", 0), "status": item.get("status", "pending")}
            elif not isinstance(item, str) and not isinstance(item, int):
                issues.append(f"Неожиданный тип в позиции {i}: {type(item)}")
        except Exception as e:
            issues.append(f"Ошибка обработки позиции {i}: {e}")
    return data, issues if issues else ["Данные целы"]

if __name__ == "__main__":
    test_data = [
        {"topic": "Python Basics", "level": 1, "status": "completed"},
        {"topic": "Data Structures", "level": 2, "status": "in_progress"},
        None,
        {"topic": "Algorithms", "level": 3},
    ]
    repaired, report = repair_and_verify(test_data)
    print(report)
    for i, item in enumerate(repaired):
        print(f"  [{i}] {item}")
