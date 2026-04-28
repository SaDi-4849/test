import csv

class Task:

    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"name: {self.name} | description: {self.description} | priority: {self.priority}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(task_name)

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                return True
        return False

    def show_tasks(self):
        if not self.tasks:
            print("you have no tasks!")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def save_to_csv(self, filename):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "description", "priority"])
            for task in self.tasks:
                writer.writerow([task.name, task.description, task.priority])

    def load_from_csv(self, filename):
        try:
            with open(filename, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.tasks.clear()
                for row in reader:
                    task = Task(row["name"], row["description"], row["priority"])
                    self.tasks.append(task)
        except FileNotFoundError:
            print("FileNotFoundError. Made a new list")
