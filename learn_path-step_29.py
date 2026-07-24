# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: LearnPath
class AppSettings:
    """Конфигурация приложения через словарь настроек"""

    def __init__(self):
        self._settings = {
            "app_name": "LearnPath",
            "default_language": "en",
            "progress_bar_length": 20,
            "max_lessons_per_day": 5,
            "streak_bonus_threshold": 7,
            "level_up_points": 100,
            "lesson_difficulty_levels": ["beginner", "intermediate", "advanced"],
            "practice_modes": ["drill", "quiz", "flashcards"],
            "checkpoint_interval_lessons": 3,
        }

    def get(self, key: str):
        return self._settings.get(key)

    def set(self, key: str, value):
        if key not in self._settings:
            raise ValueError(f"Unknown setting: {key}")
        self._settings[key] = value

    def to_dict(self):
        return dict(self._settings)

    @classmethod
    def load_from_dict(cls, config_dict):
        app = cls()
        for key, value in config_dict.items():
            app.set(key, value)
        return app


# Пример использования:
if __name__ == "__main__":
    settings = AppSettings()
    print(f"Приложение: {settings.get('app_name')}")
    settings.set("default_language", "ru")
    print(f"Язык по умолчанию: {settings.get('default_language')}")
    print(f"Настройки: {settings.to_dict()}")
