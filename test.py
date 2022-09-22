



from task_scheduler import Task, TaskScheduler 
from datetime import time

task = Task("#123",'Wash the plates',time(10,0),time(10,30))
schdlr = TaskScheduler()
schdlr.add_task(task.generate_task_profile())