tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def view_tasks():
    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index + 1}. {task['task']} - {status}")

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    else:
        print("Invalid task number")

def mark_task_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
    else:
        print("Invalid task number")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Mark a task as done")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            index = int(input("Enter the task number to delete: ")) - 1
            delete_task(index)
        elif choice == "4":
            view_tasks()
            index = int(input("Enter the task number to mark as done: ")) - 1
            mark_task_done(index)
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
