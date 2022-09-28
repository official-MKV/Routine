from task_scheduler import Task, TaskScheduler
from task_manager import Manager
from datetime import time
task= Task(
    12325343,
    'Afternoon Jogging',
    time(10,40),
    time(10,32)
)

schdlr = TaskScheduler()
schdlr.add_task(task)
dbmngr = Manager()
dbmngr.add_data(task)
 

