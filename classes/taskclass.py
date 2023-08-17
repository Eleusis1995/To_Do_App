from enum import Enum, IntEnum
import json

class Priority(IntEnum):
    LOW = 0
    Medium = 1
    HIGH = 2
    SUPER = 3

DATA_BASE_PATH = "database\tasks_database.json"

class Category(Enum):
    SCHOOL = "School",
    WOEK = "Work",
    PERSONAL = "Personal"

class Task:
    def __init__(self, tittle:str, description:str,duedate:str,priority:Priority=Priority.Medium,
                 cathegory:Category = Category.PERSONAL,outdate:bool=False,completed:bool=False) -> None:
        self.tittle = tittle
        self.description = description
        self.duedate = duedate
        self.priority = priority
        self.cathegory = cathegory
        self.outdate = outdate
        self.completed = completed

    def __repr__(self) -> str:
        return f"Task({self.tittle}, {self.description}, {self.duedate}, {self.priority}, {self.cathegory}, {self.outdate}, {self.completed})"

class TaskManager:
    
    def __init__(self, ) -> None:
        self.mytasklist = []

    def add_new_task(self,new_task:Task):
        if not isinstance(new_task,Task):
            raise TypeError("This is not Type 'Task'")
        self.mytasklist.append(Task)
        with open(DATA_BASE_PATH, "w") as f:
            json.dump(self.mytasklist, f)
