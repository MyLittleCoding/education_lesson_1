# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: LearnPath
def print_table(data: list[tuple], headers: list[str]) -> None:
    """Выводит список кортежей в компактную текстовую таблицу."""
    if not data or not headers:
        return
    widths = [len(str(h)) for h in headers] + [max(len(str(row[i])) for row in data) for i in range(len(headers))]
    fmt = " | ".join(f"{{:<{w}}}" for w in widths)
    print(fmt.format(*headers))
    print("-+-".join("-" * w for w in widths))
    for row in data:
        print(fmt.format(*row))

def show_progress(progress_data: list[tuple], progress_headers: list[str]) -> None:
    """Демонстрация прогресса обучения в виде таблицы."""
    print_table(progress_data, progress_headers)
