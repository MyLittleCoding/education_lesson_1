# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: LearnPath
def search_courses(query, fields=None):
    if not query:
        return courses_list.copy()
    query = query.lower().strip()
    if fields is None:
        fields = ['title', 'description']
    results = []
    for course in courses_list:
        match = False
        for field in fields:
            text = str(course.get(field, '')).lower()
            if query in text:
                match = True
                break
        if match:
            results.append(course.copy())
    return results
