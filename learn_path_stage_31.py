# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: LearnPath
class ProfileManager:
    def __init__(self, profiles_dir="profiles"):
        self.profiles_dir = profiles_dir

    def _profile_path(self, name):
        return os.path.join(self.profiles_dir, f"{name}.json")

    def load_profiles(self):
        profiles = {}
        if not os.path.exists(self.profiles_dir):
            os.makedirs(self.profiles_dir)
        for fname in os.listdir(self.profiles_dir):
            if fname.endswith(".json"):
                name = fname[:-5]
                with open(self._profile_path(name)) as f:
                    profiles[name] = json.load(f)
        return profiles

    def save_profile(self, name, data):
        path = self._profile_path(name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + ".tmp"
        with open(tmp, "w") as f:
            json.dump(data, f, indent=2)
        os.replace(tmp, path)

    def set_active_profile(self, name):
        profiles = self.load_profiles()
        if name not in profiles:
            raise ValueError(f"Профиль '{name}' не найден. Доступные: {list(profiles.keys())}")
        active_path = os.path.join(self.profiles_dir, "active.json")
        with open(active_path, "w") as f:
            json.dump({"profile": name}, f)
        return profiles[name]

    def get_active_profile(self):
        if not os.path.exists(os.path.join(self.profiles_dir, "active.json")):
            raise RuntimeError("Нет активного профиля. Выбери профиль через set_active_profile().")
        with open(os.path.join(self.profiles_dir, "active.json")) as f:
            return json.load(f)["profile"]

    def delete_profile(self, name):
        if os.path.exists(self._profile_path(name)):
            os.remove(self._profile_path(name))
        if not os.path.exists(self.profiles_dir):
            os.makedirs(self.profiles_dir)


# Пример использования:
if __name__ == "__main__":
    pm = ProfileManager()
    # Создаём несколько профилей (имитация данных, если файл не создан ранее)
    for name in ["novice", "intermediate", "advanced"]:
        if not os.path.exists(pm._profile_path(name)):
            pm.save_profile(name, {"level": 1, "lessons_done": 0, "streak_days": 0})

    print("Доступные профили:", pm.load_profiles().keys())
    active = pm.get_active_profile()
    print(f"Текущий активный профиль: {active}")

    # Переключение на другой профиль
    new_active = pm.set_active_profile("advanced")
    print(f"\nПереключились на: {new_active['level']} (уровень)")

    # Удаление профиля (симуляция)
    if os.path.exists(pm._profile_path("novice")):
        pm.delete_profile("novice")
        print("\nУдалили профиль 'novice'")

    print(f"\nАктивный после изменений: {pm.get_active_profile()}")
