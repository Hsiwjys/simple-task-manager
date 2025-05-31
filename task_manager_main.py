from task_management_system.task_manager import TaskManager
def main():
    print("Welcome to the Simple Task Manager!\n")

    # 1) Instantiate TaskManager exactly once
    manager = TaskManager()

    is_running = True
    while is_running:
        print("1. Add Task\n2. View Tasks\n3. Exit")

        choice_str = input("Enter your Choice: ").strip()

        # Convert to int or re‐prompt if invalid
        try:
            user_choice = int(choice_str)
        except ValueError:
            print("❌ Please enter a number (1, 2, or 3).")
            continue

        # Dispatch based on the integer choice
        match user_choice:
            case 1:
                # 2) Call add_task on the INSTANCE (self is filled automatically)
                manager.add_task()
            case 2:
                manager.view_task()
            case 3:
                is_running = False

    print("Goodbye!")


if __name__ == "__main__":
    main()
