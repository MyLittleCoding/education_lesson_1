# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: LearnPath
def parse_date(date_str):
    """Парсинг даты в формате 'YYYY-MM-DD'. Возвращает datetime.date или вызывает SystemExit."""
    import sys
    try:
        parts = date_str.strip().split('-')
        if len(parts) != 3 or any(not p.isdigit() for p in parts):
            raise ValueError("Неверный формат даты. Ожидается YYYY-MM-DD.")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        if not (1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError("Диапазон значений за пределами допустимого.")
    except (ValueError, IndexError):
        print(f"Ошибка: '{date_str}' не является корректной датой в формате YYYY-MM-DD.", file=sys.stderr)
        sys.exit(1)
    return datetime.date(year, month, day)

from datetime import date as dt_date

# Пример использования:
try:
    d = parse_date("2024-12-31")
    print(f"Парсинг успешен: {d}")
except SystemExit:
    pass
