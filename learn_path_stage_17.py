# === Stage 17: Добавь группировку записей по категориям ===
# Project: LearnPath
from collections import defaultdict

def group_by_category(records):
    grouped = defaultdict(list)
    for record in records:
        category = record.get('category', 'Uncategorized')
        grouped[category].append(record)
    return dict(grouped)

# Пример использования (раскомментируйте для теста):
# raw_data = [
#     {'id': 1, 'title': 'Введение в Python', 'category': 'Основы'},
#     {'id': 2, 'title': 'Структуры данных', 'category': 'Основы'},
#     {'id': 3, 'title': 'Работа с API', 'category': 'Практика'}
# ]
# print(group_by_category(raw_data))
