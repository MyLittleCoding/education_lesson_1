# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: LearnPath
def sort_records(records, key='date'):
    if not records: return []
    reverse = False
    if key == 'priority':
        def _cmp(r): return -r['priority']
        reverse = True
    elif key == 'name':
        def _cmp(r): return r['name'].lower()
    else: # date or default
        def _cmp(r): return r.get(key, float('inf')) if isinstance(r[key], str) else r[key]
    return sorted(records, key=_cmp, reverse=reverse)
