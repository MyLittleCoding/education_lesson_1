# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: LearnPath
class TagManager:
    def __init__(self):
        self.tags = {}  # {tag_name: set of lesson_ids}

    def add_tag(self, tag_name: str, lesson_id: int) -> bool:
        if not tag_name.strip():
            return False
        if tag_name.lower() in self.tags and lesson_id in self.tags[tag_name.lower()]:
            return True  # Already exists
        self.tags.setdefault(tag_name.lower(), set()).add(lesson_id)
        return True

    def remove_tag(self, tag_name: str, lesson_id: int) -> bool:
        if not tag_name.strip():
            return False
        lower = tag_name.lower()
        if lower in self.tags and lesson_id in self.tags[lower]:
            self.tags[lower].remove(lesson_id)
            if not self.tags[lower]:
                del self.tags[lower]
            return True
        return False

    def get_lessons_by_tag(self, tag_name: str) -> list[int]:
        lower = tag_name.lower()
        return sorted(list(self.tags.get(lower, set())))

    def remove_all_tags_for_lesson(self, lesson_id: int):
        to_remove = [tag for tag in self.tags if lesson_id in self.tags[tag]]
        for tag in to_remove:
            del self.tags[tag]
