# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: LearnPath
def project_metrics():
    """Считает ключевые метрики проекта."""
    total_lessons = len(LESSONS)
    total_practices = len(PRACTICES)
    total_milestones = len(MILESTONES)
    total_todos = sum(len(t['items']) for t in TODOS)
    completed_todos = sum(sum(1 for i in t['items'] if i.get('done', False)) for t in TODOS)
    progress = (completed_todos / total_todos * 100) if total_todos > 0 else 0.0
    print(f"📊 Метрики проекта:\n   Уроки: {total_lessons}\n   Практики: {total_practices}\n   Контрольные точки: {total_milestones}\n   Задачи всего: {total_todos}\n   Выполнено задач: {completed_todos}\n   Прогресс: {progress:.1f}%")
