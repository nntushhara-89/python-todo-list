
tasks = []


def show_tasks():
    if not tasks:
        print("Your to-do list is empty.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['name']} - {status}")


def add_task():
    name = input("Enter a task: ").strip()

    if name:
        tasks.append({"name": name, "completed": False})
        print("Task added successfully!")
    else:
        print("Task name cannot be empty.")


def complete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter the task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter the task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Deleted task: {removed['name']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
