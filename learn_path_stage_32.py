# === Stage 32: Добавь журнал действий пользователя ===
# Project: LearnPath
class ActionLog:
    def __init__(self, path="learnpath_actions.json"):
        self.path = path
        import json
        self._data = []
        try:
            with open(self.path) as f:
                self._data = json.load(f)
        except FileNotFoundError:
            pass

    def log(self, action_type, content):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action_type": action_type,
            "content": content
        }
        self._data.append(entry)
        with open(self.path, "w") as f:
            json.dump(self._data, f, indent=2)

    def get_logs(self):
        return list(reversed(self._data))
