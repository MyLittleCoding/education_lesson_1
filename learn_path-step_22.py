# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: LearnPath
def check_overdue_reminders():
    overdue = []
    for item in all_items:
        if (item.get("type") == "lesson" or item.get("type") == "practice") and \
           item.get("scheduled_date") and \
           datetime.now().date() > datetime.strptime(item["scheduled_date"], "%Y-%m-%d").date():
            overdue.append({**item, "status": "overdue"})
    return overdue

if check_overdue_reminders():
    print(f"⚠️  Просрочено {len(check_overdue_reminders())} элементов!")
else:
    print("✅ Все в порядке, ничего не просрочено.")
