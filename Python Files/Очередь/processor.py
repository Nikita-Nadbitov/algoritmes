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
        self.p1_time_work = 0
        self.p1_task_type = None
        self.p2_time_work = 0
        self.p2_task_type = None

    def add_task(self, task: Task):
        if task.get_type() in [0,1]:
            if self.p1.idle:
                self.p1_time_work = task.get_time()
                self.p1_task_type = task.get_type()
                self.p1.idle = False
            elif self.p2.idle:
                self.p2_time_work = task.get_time()
                self.p2_task_type = task.get_type()
                self.p2.idle = False
        elif task.get_type() == 2:
            if self.p2.idle:
                self.p2_time_work = task.get_time()
                self.p2_task_type = task.get_type()
                self.p2.idle = False
            elif self.p1.idle:
                self.p1_time_work = task.get_time()
                self.p1_task_type = task.get_type()
                self.p1.idle = False

    def __task_perform_p1(self):
        self.p1_time_work -= 1
        if self.p1_time_work <= 0:
            self.p1.idle = True
            self.p1_task_type = None

    def __task_perform_p2(self):
        self.p2_time_work -= 1
        if self.p2_time_work <= 0:
            self.p2.idle = True
            self.p2_task_type = None

    def __str__(self):
        string = "|proc|type|time|idle|"
        if not self.p1.idle:
            string += "\n|1   |{:<4}|{:<4}|{:<4}|".format(str(self.p1_task_type), str(self.p1_time_work), str(self.p1.idle))
        else:
            string += "\n|1   |None|None|True|"
        if not self.p2.idle:
            string += "\n|2   |{:<4}|{:<4}|{:4}|".format(str(self.p2_task_type), str(self.p2_time_work), str(self.p2.idle))
        else:
            string += "\n|2   |None|None|True|"
        string += "\n|{:<4}|{:<4}|{:<4}|{:<4}|\n\n".format("____", "____", "____", "____")
        return string

    def work(self):
        if not self.p1.idle:
            self.__task_perform_p1()
        else:
            self.p1.idle = True
        if not self.p2.idle:
            self.__task_perform_p2()
        else:
            self.p2.idle = True

    def idle_proc(self):
        return self.p2.idle or self.p1.idle