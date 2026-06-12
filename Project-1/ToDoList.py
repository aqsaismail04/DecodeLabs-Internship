# To-Do List Application

tasks = []

# Load existing tasks from file
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    pass

print("===== Welcome to My To-Do List =====")

while True:
    print("\nMenu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)

        with open("tasks.txt", "a") as file:
            file.write(task + "\n")

        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        print("Thank you for using the To-Do List App. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")