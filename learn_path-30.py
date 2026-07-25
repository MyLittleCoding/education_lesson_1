# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: LearnPath
class Profile:
    def __init__(self, name, goals=None):
        self.name = name
        self.goals = goals or []

    @staticmethod
    def create(name, goals=None):
        return Profile(name, goals)

    def add_goal(self, goal):
        if goal not in self.goals:
            self.goals.append(goal)

    def remove_goal(self, goal):
        self.goals.remove(goal)

    def has_goal(self, goal):
        return goal in self.goals

class ProfileManager:
    def __init__(self):
        self.profiles = {}

    def get_profile(self, name):
        if name not in self.profiles:
            self.profiles[name] = Profile(name)
        return self.profiles[name]

    def delete_profile(self, name):
        del self.profiles[name]
