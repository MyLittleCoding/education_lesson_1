# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: LearnPath
def archive_completed_records(records, target_dir="archives"):
    """Archive records with status 'completed' or older than 30 days."""
    import os, shutil, datetime
    os.makedirs(target_dir, exist_ok=True)
    archived = []
    for rec in records:
        if rec.get("status") == "completed" and rec.get("completed_at"):
            age_days = (datetime.datetime.now() - datetime.datetime.fromisoformat(rec["completed_at"])).days
            if age_days >= 30 or rec.get("created_at"):
                age_days2 = (datetime.datetime.now() - datetime.datetime.fromisoformat(rec["created_at"])).days
                if age_days2 >= 30:
                    archived.append(rec)
    for rec in archived:
        filename = f"record_{rec['id']}.json"
        filepath = os.path.join(target_dir, filename)
        with open(filepath, "w") as f:
            json.dump(rec, f, indent=2)
