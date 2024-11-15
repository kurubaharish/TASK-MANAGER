import json

# Dummy credentials
DUMMY_EMAIL = "test@example.com"
DUMMY_PASSWORD = "password123"

class Task:
    def _init_(self, id: int, title: str):
        self.id = id
        self.title = title
        self.completed = False

    def _repr_(self):
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"

# Initialize an empty list to store tasks
tasks = []

def login(email: str, password: str):
    """Simulate user login with dummy credentials."""
    if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False

def add_task(title: str):
    """Adds a new task with the given title to the task list."""
    task_id = len(tasks) + 1  # Simple ID assignment
    new_task = Task(task_id, title)
    tasks.append(new_task)
    print(f"Added task: {new_task}")

def view_tasks():
    """Displays all tasks along with their completion status."""
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        status = "Completed" if task.completed else "Not Completed"
        print(f"[{task.id}] {task.title} - {status}")

def delete_task(task_id: int):
    """Deletes a task by its ID."""
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    print(f"Deleted task with ID: {task_id}")

def mark_task_complete(task_id: int):
    """Marks a task as completed by its ID."""
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            print(f"Marked task as complete: {task}")
            return
    print(f"No task found with ID: {task_id}")

def save_tasks(filename='tasks.json'):
    """Saves the current list of tasks to a JSON file."""
    with open(filename, 'w') as file:
        json.dump([task._dict_ for task in tasks], file)
    print("Tasks saved to file.")

def load_tasks(filename='tasks.json'):
    """Loads tasks from a JSON file into the application."""
    global tasks
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            tasks = [Task(**data) for data in tasks_data]
            print("Tasks loaded from file.")
    except FileNotFoundError:
        print("No saved tasks found.")

def main():
    load_tasks()  # Load existing tasks at startup
    
    # Simulate login
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if not login(email, password):
        return  # Exit if login fails

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save Tasks")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            mark_task_complete(task_id)
        elif choice == '5':
            save_tasks()
        elif choice == '6':
            save_tasks()  # Save before exiting
            print("Exiting application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()