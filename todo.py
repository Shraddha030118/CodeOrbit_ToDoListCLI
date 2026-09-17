tasks = []


def add_task():
    print("\n--- Add Task ---")
    task = input("Enter your task: ")

    if task.strip():
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def view_tasks():
    print("\n--- Your Tasks ---")

    if not tasks:
        print("No tasks available.")
        return

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def remove_task():
    print("\n--- Remove Task ---")

    if not tasks:
        print("No tasks available.")
        return

    view_tasks()

    try:
        number = int(input("Enter the task number to remove: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Task removed: {removed}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n========================")
        print("      TO-DO LIST APP")
        print("========================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            print("Thank you for using the To-Do List App!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()