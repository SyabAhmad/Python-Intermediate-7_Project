print("To-Do List using Python")
# Define an empty list to store the tasks
tasks = []

# Define a function to add a new task to the list
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)

# Define a function to remove a task from the list
def remove_task():
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found")

# Define a function to display the list of tasks
def display_tasks():
    if not tasks:
        print("No tasks to display")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

# Define a function to mark a task as completed
def complete_task():
    task = input("Enter the task to mark as completed: ")
    if task in tasks:
        index = tasks.index(task)
        tasks[index] = f"[x] {task}"
    else:
        print("Task not found")

# Define a function to sort the list of tasks
def sort_tasks():
    tasks.sort()

# Define a function to display the menu and handle user input
def main():
    while True:
        print("""
        To-do List Manager

        1. Add a task
        2. Remove a task
        3. Display tasks
        4. Mark a task as completed
        5. Sort tasks
        6. Quit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            sort_tasks()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

