from task_scheduler import Task, TaskScheduler
from task_manager import Manager
from datetime import time
task= Task(
    12325343,
    'Afternoon Reading',
    time(12,30),
    time(15,0)
)

# schdlr = TaskScheduler()
# schdlr.add_task(task)
dbmngr = Manager()
dbmngr.add_data(task)
