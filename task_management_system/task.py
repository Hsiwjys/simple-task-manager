from datetime import date
class Task:
    def __init__(self, task_id: int, task_name: str, description: str, due_date: date):
        # Store them “privately” (name‐mangled) so there’s no direct external assignment
        self.__task_id = task_id
        self.__task_name = task_name
        self.__description = description
        self.__due_date = due_date

    @property
    def task_id(self) -> int:
        return self.__task_id

    @property
    def task_name(self) -> str:
        return self.__task_name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def due_date(self) -> date:
        return self.__due_date
