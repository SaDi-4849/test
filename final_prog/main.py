from final_prog import Task, ToDoList


def main():
    todo_list = ToDoList()
    filename = "tasks.csv"
    todo_list.load_from_csv(filename)

    while True:
       
        print("")
        print("------ ToDoList menu ------")
        print("Add task: 1")
        print("Remove task: 2")
        print("Show taskslist : 3")
        print("Save list in file: 4")
        print("Exit: 5")
        print("")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                try:
                    name = input("Enter task name: ").strip()
                    description = input("Enter task description: ").strip()
                    priority = (
                        input("Enter task priority (high /medium /low): ").strip().lower()
                    )

                    if priority not in ["high", "medium", "low"]:
                        raise ValueError("Priority must be 'high', 'medium', or 'low'.")

                    task = Task(name, description, priority)
                    todo_list.add_task(task)
                    print(" Task added successfully.")
                    break
                except Exception as e:
                    print(f" Error: {e} | try again")

        elif choice == "2":
            name = input("Enter task name(or enter 0 to remove ALL tasks): ").strip()
            if name == "0":
                confirm = (
                    input("are you sure you want to remove all tasks? yes/no: ")
                    .strip()
                    .lower()
                )
                if confirm == "yes":
                    todo_list.tasks.clear()
                    print(" All tasks have been deleted.")
                else:
                    print("Operation cancelled.")

            else:
                if todo_list.remove_task(name):
                    print("Task removed.")
                else:
                    print("No task with this name.")

        elif choice == "3":
            todo_list.show_tasks()

        elif choice == "4":
            todo_list.save_to_csv(filename)
            print("Task successfully saved.")
            break

        elif choice == "5":
            print("exiting program")
            break

        else:
            print("must be a number between 1-5. try again")


if __name__ == "__main__":
    main()
