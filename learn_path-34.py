# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: LearnPath
class Template:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields  # {field_name: default_value}

    def create_record(self, user_input=None):
        record = {}
        for field, default in self.fields.items():
            if field == 'id':
                continue
            value = user_input.get(field) if user_input else None
            if value is None and default is not None:
                value = default
            record[field] = value
        return record

templates_db = []

def add_template(name, fields):
    templates_db.append(Template(name, fields))

def list_templates():
    for t in templates_db:
        print(f"  - {t.name}: {t.fields}")

def create_from_template(template_name, user_input=None):
    template = None
    for t in templates_db:
        if t.name == template_name:
            template = t
            break
    if not template:
        return "Template not found"
    record = template.create_record(user_input)
    records.insert(0, record)
    print(f"Record created from {template_name}")
    return record

add_template("Lesson", {"title": "", "duration_minutes": 30})
add_template("Practice", {"description": "", "difficulty": "medium"})
