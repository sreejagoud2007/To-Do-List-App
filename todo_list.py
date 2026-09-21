tasks = []

def add_task():
    task = input("Enter a new task: ")

    if task.strip():
        tasks.append({"title": task, "completed": False})
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n--- To-Do List ---")

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} - {status}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter the task number to complete: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter the task number to delete: "))

        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['title']}' deleted successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== TO-DO LIST APP =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()