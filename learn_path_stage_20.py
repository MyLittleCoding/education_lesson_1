# === Stage 20: Добавь восстановление записей из архива ===
# Project: LearnPath
import json, os

def restore_from_archive(archive_path, config_path):
    if not os.path.exists(archive_path) or not os.path.exists(config_path):
        print("❌ Архив не найден.")
        return False
    with open(archive_path, 'r', encoding='utf-8') as f:
        archive = json.load(f)
    print(f"📂 Архив загружен из {archive_path}")
    print(f"   — {len(archive.get('lessons', []))} уроков")
    print(f"   — {len(archive.get('practices', []))} практик")
    print(f"   — {len(archive.get('milestones', []))} контрольных точек")
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    for key in ['lessons', 'practices', 'milestones']:
        if key not in archive or len(archive[key]) == 0:
            continue
        existing_ids = {item['id'] for item in config.get(key, [])}
        new_items = [item for item in archive[key] if item['id'] not in existing_ids]
        if new_items:
            config[key].extend(new_items)
            print(f"✅ Восстановлено {len(new_items)} записей из архива.")
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    return True

restore_from_archive('learnpath/archive.json', 'learnpath/config.json')
