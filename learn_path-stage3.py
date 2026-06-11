# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: LearnPath
class LearningPath:
    def __init__(self):
        self._lessons = []
        self._practices = []
        self._milestones = []
        self._progress = {}

    def add_lesson(self, title: str, duration_minutes: int) -> None:
        lesson_id = len(self._lessons) + 1
        record = {
            "id": lesson_id,
            "title": title,
            "duration_minutes": duration_minutes,
            "status": "pending",
            "completed_at": None
        }
        self._lessons.append(record)

    def add_practice(self, description: str, estimated_time_minutes: int) -> None:
        practice_id = len(self._practices) + 1
        record = {
            "id": practice_id,
            "description": description,
            "estimated_time_minutes": estimated_time_minutes,
            "status": "pending",
            "completed_at": None
        }
        self._practices.append(record)

    def add_milestone(self, title: str, target_lesson_ids: list[int]) -> None:
        milestone_id = len(self._milestones) + 1
        record = {
            "id": milestone_id,
            "title": title,
            "target_lesson_ids": target_lesson_ids,
            "achieved": False
        }
        self._milestones.append(record)

    def mark_completed(self, lesson_id: int) -> None:
        for lesson in self._lessons:
            if lesson["id"] == lesson_id and not lesson["completed_at"]:
                import datetime
                lesson["status"] = "completed"
                lesson["completed_at"] = datetime.datetime.now().isoformat()

    def get_total_progress(self) -> float:
        total_lessons = len(self._lessons)
        if total_lessons == 0:
            return 0.0
        completed_count = sum(1 for l in self._lessons if l["status"] == "completed")
        return round((completed_count / total_lessons) * 100, 2)
