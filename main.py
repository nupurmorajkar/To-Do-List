tasks = []

while True:
    print("\n    TO DO LIST")
    print("1. VIEW TASKS")
    print("2. ADD TASK")
    print("3. REMOVE TASK")
    print("4. EXIT")

    choice = input("Enter your choice:")

    if choice == "1":
        if len(tasks) == 0:
            print("No task to do")
        else:
            print("\n Tasks :")
            for task in tasks:
                print("-", task)

    elif choice == "2":
        task = input("Enter task to add: ")
        tasks.append(task)
        print("Task added successfully")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove")
        else:
            task = input("Enter task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print("Task removed from list")
            else:
                print("Task not found")

    elif choice == "4":
        print("Exiting the program...")
        break       

    else:
        print("Invalid choice. Please try again sorry.")