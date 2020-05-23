from processor import Processor
from queue import Queue
from task import Task
from stack import Stack

if __name__ == "__main__":
    proc = Processor()
    task_queue = Queue()
    task_stack = Stack()
    while True:
        a = Task()
        task_queue.add_task(a)
        if proc.idle_proc():
            if not task_queue.get_queue_empty_flag():
                proc.add_task(task_queue.del_task())
            elif not task_stack.check_is_empty():
                proc.add_task(task_stack.del_item())
        else:
            if not task_queue.get_queue_empty_flag():
                task_stack.add_item(task_queue.del_task())
        print(proc)
        print(task_stack)
        print(task_queue)
        proc.work()