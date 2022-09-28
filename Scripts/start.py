from ast import If
import time
import argparse
import sys
import json
from playsound import playsound
sys.path.append('C:\\Users\\vemma\\Desktop\\Routine') ## TODO: fix this
from task_manager import Manager
from VoiceAssistant import Assistant
 
 

if __name__=="__main__":
    arg = sys.argv[1]
    va = Assistant()
    db = Manager()
    task_id = arg[:len(arg)-1]
    playsound('C:\\Users\\vemma\\Desktop\\Routine\\Resources\\beep.mp3') # NOTE playsound had to be downgraded there seems to be an issue with the latest version
    task = db.get_task(task_id)
    name = task["name"]
    va.say(f"Time to f{task.name}")
    ## TODO
    # Recieve input to update task if necessary
     
     
