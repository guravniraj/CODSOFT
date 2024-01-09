tasks = []
def add_task(task):
    tasks.append({"task": task, "done": False})
    print("Task added successfully!💯")

def list_tasks():
    if not tasks:
        print("No tasks in the list.😕")
    else:
        for index, task in enumerate(tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index + 1}. {task['task']} - {status}")

def mark_task_done(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        print("Task marked as done!😊")
    else:
        print("Invalid task number😓.")

def delete_task(index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        print("Task deleted successfully!👍")
    else:
        print("Invalid task number.👎")

while True:
    print("\n✍️ To-Do List Menu - By Niraj Gurav")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        index = int(input("Enter task number to mark as done: "))
        mark_task_done(index)
    elif choice == "4":
        index = int(input("Enter task number to delete: "))
        delete_task(index)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")