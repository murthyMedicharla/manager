
tasks = []

while True:
    print("\n---- TO DO LIST MANAGER ----")
    print("1. View Task")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks in the list.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, task)

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "3":
        task_no = int(input("Enter task number to remove: "))
        if 0 < task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print("Removed task:", removed)
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")