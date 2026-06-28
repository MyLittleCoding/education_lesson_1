# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: LearnPath
def calculate_weekly_stats(lessons, practices, checkpoints):
    from datetime import date, timedelta
    
    if not lessons and not practices:
        return []
    
    all_activities = list(lessons) + list(practices)
    if checkpoints:
        for c in checkpoints:
            if isinstance(c, dict):
                all_activities.append({'date': c.get('completed_at'), 'type': 'checkpoint', 'id': c['id']})
            else:
                all_activities.append({'date': c.date(), 'type': 'checkpoint', 'id': c.id})
    
    start_date = min(a['date'] for a in all_activities if isinstance(a.get('date'), date))
    end_date = max(a['date'] for a in all_activities if isinstance(a.get('date'), date))
    
    weekly_stats = []
    current_week_start = start_date - timedelta(days=start_date.weekday())
    week_num = 1
    
    while current_week_start <= end_date:
        week_end = current_week_start + timedelta(weeks=1)
        
        week_lessons = sum(1 for a in all_activities if isinstance(a.get('date'), date) and 
                          current_week_start <= a['date'] < week_end and a['type'] == 'lesson')
        week_practices = sum(1 for a in all_activities if isinstance(a.get('date'), date) and 
                            current_week_start <= a['date'] < week_end and a['type'] == 'practice')
        week_checkpoints = sum(1 for a in all_activities if isinstance(a.get('date'), date) and 
                               current_week_start <= a['date'] < week_end and a['type'] == 'checkpoint')
        
        weekly_stats.append({
            'week': week_num,
            'start_date': current_week_start.isoformat(),
            'end_date': (current_week_start + timedelta(days=6)).isoformat(),
            'lessons_count': week_lessons,
            'practices_count': week_practices,
            'checkpoints_passed': week_checkpoints
        })
        
        current_week_start += timedelta(weeks=1)
        week_num += 1
    
    return weekly_stats
