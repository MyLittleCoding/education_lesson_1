# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: LearnPath
def main():
    lessons = [
        {"id": 1, "title": "Введение в Python", "type": "lesson"},
        {"id": 2, "title": "Переменные и типы данных", "type": "practice"},
        {"id": 3, "title": "Условные операторы", "type": "checkpoint"},
    ]

    print("=== LearnPath: Планировщик обучения ===")
    while True:
        print("\nМеню действий:")
        print("1. Показать список уроков")
        print("2. Пройти урок по ID")
        print("3. Выйти из программы")
        choice = input("Ваш выбор (1-3): ").strip()

        if choice == "1":
            for item in lessons:
                status = "✓" if item["type"] != "lesson" else "-"
                print(f"[{status}] ID {item['id']}: {item['title']} ({item['type'].capitalize()})")
        elif choice == "2":
            try:
                lesson_id = int(input("Введите ID урока для прохождения: "))
                lesson = next((l for l in lessons if l["id"] == lesson_id), None)
                if lesson:
                    print(f"\nВы начали урок: {lesson['title']}")
                    # Имитация прогресса без задержек
                    input("Нажмите Enter, когда закончите...")
                    status = "✓" if lesson["type"] != "lesson" else "-"
                    print(f"[{status}] Урок '{lesson['title']}' пройден!")
                else:
                    print("Урок с таким ID не найден.")
            except ValueError:
                print("Ошибка: введите числовое значение.")
        elif choice == "3":
            print("До свидания! Спасибо, что использовали LearnPath.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()
