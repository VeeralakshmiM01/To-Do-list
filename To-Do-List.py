# To-Do List Application

# Initialize an empty list to store tasks
tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{index}. {task['task']} - {status}")

def mark_task_completed(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print(f"Task '{tasks[task_index - 1]['task']}' marked as completed.")
    else:
        print("Invalid task index.")

def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Task '{deleted_task['task']}' deleted.")
    else:
        print("Invalid task index.")

if __name__ == "__main__":
    while True:
        print("\n===== To-Do List Application =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_index = int(input("Enter task index to mark as completed: "))
            mark_task_completed(task_index)
        elif choice == '4':
            task_index = int(input("Enter task index to delete: "))
            delete_task(task_index)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
