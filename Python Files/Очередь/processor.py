from dataclasses import dataclass
from task import Task

@dataclass()
class ProcessorOne:
    current_task: Task = None
    idle: bool = True

@dataclass()
class ProcessorTwo:
    current_task: Task = None
    idle: bool = True

class Processor():

    def __init__(self):
        self.p1 = ProcessorOne
        self.p2 = ProcessorTwo

    def add_task(self, task: Task):
        task_type = task.get_type

