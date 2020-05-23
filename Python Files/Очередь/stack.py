from  dataclasses import dataclass

@dataclass()
class TaskStack:
    list_of_task = []
    is_empty = True
    length = 0

class Stack:
    def __init__(self):
        self.stack = TaskStack

    def add_item(self, task):
        self.stack.list_of_task.append(task)
        self.stack.length += 1
        self.stack.is_empty = False

    def del_item(self):
        if self.stack.length != 0:
            self.stack.length -= 1
            if self.stack.length == 0:
                self.stack.is_empty = True
            return self.stack.list_of_task.pop(len(self.stack.list_of_task)-1)
        return -1

    def check_is_empty(self):
        return self.stack.is_empty

    def get_length(self):
        return self.stack.length

    def __str__(self):
        string = "|type|time|"
        if not self.stack.is_empty:
            for task in self.stack.list_of_task:
                string += "\n|{:<4}|{:<4}|".format(str(task.get_type()), str(task.get_time()))
        else:
            string += "\n|None|None|"
        string += "\n|____|____|\n\n"
        return string