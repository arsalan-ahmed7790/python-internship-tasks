import json

class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Task '{title}' has been added to the to-do list.")

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' has been deleted.")
                return
        print(f"Task '{title}' not found in the to-do list.")

    def view_tasks(self):
        if not self.tasks:
            print("The to-do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. Title: {task.title}, Description: {task.description}, Status: {task.status}")

    def save_tasks(self, filename="tasks.json"):
        task_data = []
        for task in self.tasks:
            task_data.append({"title": task.title, "description": task.description, "status": task.status})

        with open(filename, "w") as file:
            json.dump(task_data, file)
        print("To-do list saved to a file.")

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                task_data = json.load(file)
                self.tasks = [Task(data["title"], data["description"], data["status"]) for data in task_data]
                print("To-do list loaded from file.")
        except FileNotFoundError:
            print("No saved to-do list found.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == "2":
            title = input("Enter the title of the task to delete: ")
            todo_list.delete_task(title)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            todo_list.save_tasks()
        elif choice == "5":
            todo_list.load_tasks()
        elif choice == "6":
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
