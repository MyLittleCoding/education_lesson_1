# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: LearnPath
def generate_summary():
    if not lessons: return "Нет данных для сводки."
    total_lessons = len(lessons)
    completed_lessons = sum(1 for l in lessons if l.get('status') == 'completed')
    practice_hours = sum(l.get('practice_time', 0) for l in lessons if l['status'] == 'completed')
    checkpoints_passed = sum(1 for c in all_checkpoints if c.get('passed'))
    progress_pct = round((completed_lessons / total_lessons) * 100, 1) if total_lessons else 0.0
    return f"Прогресс: {progress_pct}% ({completed_lessons}/{total_lessons} уроков завершено).\nПрактика: {practice_hours:.1f} ч.\nКонтрольные точки пройдены: {checkpoints_passed}"
