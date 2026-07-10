# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: LearnPath
import datetime

def add_reminders():
    reminders = []
    
    def add_reminder(task, date):
        reminder = {
            'task': task,
            'date': date,
            'done': False
        }
        reminders.append(reminder)
        return reminder
    
    def get_due_reminders():
        today = datetime.date.today()
        due = [r for r in reminders if not r['done'] and r['date'] <= today]
        return due
    
    def mark_done(task):
        for r in reminders:
            if r['task'] == task and not r['done']:
                r['done'] = True
                print(f"✅ Напоминание выполнено: {r['task']}")
                break
    
    return add_reminder, get_due_reminders, mark_done

add_reminder, get_due_reminders, mark_done = add_reminders()

# Пример использования
add_reminder("Изучить Python-функции", datetime.date(2024, 1, 15))
add_reminder("Написать практику с циклами", datetime.date(2024, 1, 16))
print("Созданы напоминания")
