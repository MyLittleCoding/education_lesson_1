# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: LearnPath
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for record in records:
        if status and record.get("status") != status:
            continue
        if category and record.get("category") != category:
            continue
        if tags is not None:
            rec_tags = set(record.get("tags", []))
            if not any(tag in rec_tags for tag in tags):
                continue
        filtered.append(record)
    return filtered

def get_records_by_status(status="active"):
    return filter_records(status=status)

def get_records_by_category(category=None):
    return filter_records(category=category)

def get_records_by_tags(tags=None):
    if not tags:
        return records[:]
    tag_set = set(tags)
    filtered = []
    for record in records:
        rec_tags = set(record.get("tags", []))
        if any(tag in rec_tags for tag in tag_set):
            filtered.append(record)
    return filtered

def get_records_by_multiple_criteria(status=None, category=None, tags=None):
    return filter_records(status=status, category=category, tags=tags)
