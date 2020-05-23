from dataclasses import dataclass

from numpy import random as rnd


@dataclass()
class TaskData:
    time: int = None
    type_of_task: int = None

class Task():
    def __init__(self):
        time_work = [3, 6, 9]
        type_of_task = rnd.randint(high=3, low=0)
        self.current_task = TaskData()
        self.current_task.time = time_work[type_of_task]
        self.current_task.type_of_task = type_of_task


    def get_time(self):
        return self.current_task.time

    def get_type(self):
        return self.current_task.type_of_task