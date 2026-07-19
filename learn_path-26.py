# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: LearnPath
def main():
    print("=" * 50)
    print("DEMO COMMANDS FOR MANUAL TESTING")
    print("=" * 50)

    # --- Demo 1: Create a lesson ---
    print("\n[Demo 1] Creating a lesson...")
    lesson = Lesson(title="Python Basics", description="Learn variables, types, and control flow.",
                    duration_minutes=60, tags=["python", "beginner"])
    learn_path.lessons.append(lesson)
    print(f"Lesson created: {lesson.title}")

    # --- Demo 2: Create a practice session ---
    print("\n[Demo 2] Creating a practice session...")
    practice = PracticeSession(title="Exercises", description="Solve coding problems.",
                               duration_minutes=30, target_lessons=[lesson])
    learn_path.practices.append(practice)
    print(f"Practice created: {practice.title}")

    # --- Demo 3: Create a checkpoint ---
    print("\n[Demo 3] Creating a checkpoint...")
    checkpoint = Checkpoint(title="Mid-Course Review", description="Test your knowledge so far.",
                            questions=[
                                {"question": "What is 2 + 2?", "answer": "4"},
                                {"question": "What does print('Hello') output?", "answer": "Hello"}
                            ])
    learn_path.checkpoints.append(checkpoint)
    print(f"Checkpoint created: {checkpoint.title}")

    # --- Demo 4: Create a milestone ---
    print("\n[Demo 4] Creating a milestone...")
    milestone = Milestone(title="Python Fundamentals", description="Complete all lessons and practices.",
                           requirements=[lesson, practice], duration_days=7)
    learn_path.milestones.append(milestone)
    print(f"Milestone created: {milestone.title}")

    # --- Demo 5: Add progress updates ---
    print("\n[Demo 5] Adding progress...")
    for item in [lesson, practice, checkpoint]:
        learn_path.progress_log.append({
            "timestamp": datetime.now(),
            "type": type(item).__name__,
            "title": item.title,
            "status": "Completed" if isinstance(item, (Lesson, PracticeSession)) else "Attempted"
        })
    print(f"Progress entries: {len(learn_path.progress_log)}")

    # --- Demo 6: Summary ---
    print("\n[Demo 6] Learning Path Summary:")
    print(f"Total lessons: {len(learn_path.lessons)}")
    print(f"Total practices: {len(learn_path.practices)}")
    print(f"Total checkpoints: {len(learn_path.checkpoints)}")
    print(f"Total milestones: {len(learn_path.milestones)}")
    print(f"Progress entries: {len(learn_path.progress_log)}")

    # --- Demo 7: Print all items ---
    print("\n[Demo 7] All Items:")
    for item in learn_path.lessons + learn_path.practices + learn_path.checkpoints + learn_path.milestones:
        print(f"  - {item.title}")

if __name__ == "__main__":
    main()
