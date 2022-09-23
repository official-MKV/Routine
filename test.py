# from task_scheduler import Task, TaskScheduler
# from task_manager import Manager
# from datetime import time
# task= Task(
#     12325343,
#     'Afternoon Reading',
#     time(12,30),
#     time(15,0)
# )

# schdlr = TaskScheduler()
# schdlr.add_task(task)
# dbmngr = Manager()
# dbmngr.add_data(task)
# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices') 
# engine.setProperty('voice', voices[1].id) 
# print(engine.getProperty('rate'))
# engine.setProperty('rate', 150) 
# engine.setProperty('volume', 0.75)
# engine.say("I will speak this text")
# engine.runAndWait()