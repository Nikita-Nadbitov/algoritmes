from dataclasses import dataclass
from task import Task


@dataclass()
class QueueOne:
    list_of_task: list = []
    is_empty: bool = True

@dataclass()
class QueueTwo:
    list_of_task: list = []
    is_empty: bool = True

@dataclass()
class QueueThree:
    list_of_task: list = []
    is_empty: bool = True

class Queue():

    def __init__(self):
        self.q1 = QueueOne
        self.q2 = QueueTwo
        self.q3 = QueueThree

    def add_task(self, task:Task):
        queue_list = [self.q1, self.q2, self.q3]
        queue_list[task.get_type].list_of_task.append(task)
        queue_list[task.get_type].is_empty = False

    @property
    def del_task(self):
        if self.q1.is_empty != False:
            task = self.q1.list_of_task.pop(0)
            if len(self.q1.list_of_task) == 0:
                self.q1.is_empty = False
        elif self.q2.is_empty != False:
            task = self.q2.list_of_task.pop(0)
            if len(self.q2.list_of_task) == 0:
                self.q2.is_empty = False
        elif self.q3.is_empty != False:
            task = self.q3.list_of_task.pop(0)
            if len(self.q3.list_of_task) == 0:
                self.q3.is_empty = False
        return task

    @property
    def get_queue_empty_flag(self):
        return self.q1.is_empty, self.q2.is_empty, self.q3.is_empty
