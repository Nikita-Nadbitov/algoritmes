from dataclasses import dataclass
from numpy import random as rnd

@dataclass()
class TaskOne:
    time: int = 3
    type_of_task = 0

@dataclass()
class TaskTwo:
    time: int = 6
    type_of_task = 1

@dataclass()
class TaskThree:
    time: int = 9
    type_of_task = 2

class Task():

    def __init__(self):
        list_of_task = [TaskOne, TaskTwo, TaskThree]
        number = rnd.randint(high=3, low=0)
        self.current_task = list_of_task[number]

    @property
    def get_time(self):
        return self.current_task.time

    @property
    def get_type(self):
        return self.current_task.type_of_task
