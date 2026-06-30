# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: LearnPath
def generate_monthly_stats(lessons, practices, checkpoints):
    from datetime import date, timedelta
    
    if not lessons: return {}
    
    # Определяем диапазон дат по всем данным
    all_dates = set()
    for item in [lessons, practices, checkpoints]:
        for d in item.get('dates', []):
            try:
                all_dates.add(date.fromisoformat(d))
            except ValueError:
                pass
    
    if not all_dates: return {}
    
    min_date = min(all_dates)
    max_date = max(all_dates)
    
    # Группируем по месяцам (год-месяц -> список дат в месяце)
    months_map = {}
    current = date(min_date.year, 1, 1)
    while current <= date(max_date.year, 12, 31):
        month_key = f"{current.year}-{current.month:02d}"
        end_of_month = current.replace(day=28) + timedelta(days=(end_of_month.month % 2)) # Упрощённый конец месяца
        if current.day == end_of_month.day: break
        
        months_map[month_key] = []
        
        temp = date(current.year, current.month, 1)
        while temp <= end_of_month:
            all_dates.discard(temp)
            months_map[month_key].append(temp)
            temp += timedelta(days=1)
    
    # Формируем статистику
    stats = {}
    for month_key in sorted(months_map.keys()):
        dates_in_month = set(months_map[month_key])
        
        active_lessons = [l for l in lessons if any(d.date() == date.fromisoformat(l.get('date', '')) and d in dates_in_month for d in all_dates)] # Логика фильтрации по датам уроков
        # Упрощённая логика: считаем, если дата урока попадает в месяц
        active_lessons = [l for l in lessons if date.fromisoformat(l.get('date', '')) and date.fromisoformat(l['date']).month == int(month_key.split('-')[1])]
        
        stats[month_key] = {
            'completed_lessons': len([l for l in lessons if date.fromisoformat(l.get('date', '')).month == int(month_key.split('-')[1])]),
            'practices_count': len([p for p in practices if date.fromisoformat(p.get('date', '')).month == int(month_key.split('-')[1])]),
            'checkpoints_passed': len([c for c in checkpoints if date.fromisoformat(c.get('date', '')).month == int(month_key.split('-')[1])])
        }
    
    return stats
