from datetime import datetime, date
from .task import Task

class TaskManager:
    def __init__(self):
        # This will hold tasks by their ID, just like Java’s Map<Integer, Task>
        self.__tasks = {}
        # id_counter starts at 0 and will be incremented before assignment
        self.__id_counter = 0

    def add_task(self):
        # Prompt the user for a task name (equivalent to Scanner.nextLine())
        name = input("Enter Task Name: ").strip()
        description = input("Enter the description: ").strip()
        while True:
            date_str = input("Enter Due Date (DD-MM-YYYY): ")
            try:
                date_con = datetime.strptime(date_str, "%d-%m-%Y")
                due = date_con.date()
                today = date.today()
                if due <= today:
                    print("Given date is past date, please enter the valid date")
                    continue
                break
            except ValueError:
                print("Invalid date format, please enter the valid format ")
        # Increment the counter and use it as the new task’s ID
        self.__id_counter += 1
        task_id = self.__id_counter
        # Create a new Task and store it in the dict
        new_task = Task(task_id, name, description, due)
        self.__tasks[task_id] = new_task

        print("Task Added Successfully...")

    def view_task(self):
        if not self.__tasks:
            print("No task yet")
        # “Normal” for‐loop over keys
        for task_id in self.__tasks:
            t = self.__tasks[task_id]
            due_date = t.due_date.strftime("%d-%m-%Y")
            print(f"{task_id:}    | {t.task_name:} | {t.description} | {due_date}")
