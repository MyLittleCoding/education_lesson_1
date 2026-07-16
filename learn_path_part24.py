# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: LearnPath
def print_record(record, indent=0):
    """Выводит одну запись компактно с ключевыми деталями."""
    prefix = "  " * indent
    if isinstance(record, dict):
        name = record.get("name", "<unknown>")
        print(f"{prefix}📄 {name}")
        for key in ("id", "status", "created", "updated"):
            val = record.get(key)
            if val is not None:
                label = {"id": "ID", "status": "Статус", "created": "Дата создания", "updated": "Обновлено"}.get(key, key)
                print(f"{prefix}  • {label}: {val}")
        # Если есть children, показываем краткий подытог
        if "children" in record:
            kids = record["children"]
            total = len(kids)
            done = sum(1 for k in kids if isinstance(k, dict) and k.get("status") == "done")
            print(f"{prefix}  • Записей: {total}, готово: {done}/{total}")
    elif isinstance(record, list):
        print(f"{prefix}— список из {len(record)} элементов —")
        for item in record[:3]:
            if isinstance(item, dict):
                print(f"{prefix}  • {item.get('name', 'item')} [{item.get('status', '?')}]")
        if len(record) > 3:
            print(f"{prefix}  ... ещё {len(record)-3}")
    else:
        print(f"{prefix}{record}")
