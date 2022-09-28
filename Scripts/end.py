from ast import If
import time
import argparse
import sys
import json
from playsound import playsound
sys.path.append('C:\\Users\\vemma\\Desktop\\Routine') ## TODO: fix this
from task_manager import Manager
from  VoiceAssistant import Assistant
 
 

if __name__=="__main__":
    arg = sys.argv[1]
    task_id = arg[:len(arg)-1]
    db = Manager()
    va = Assistant()
    playsound('C:\\Users\\vemma\\Desktop\\Routine\\Resources\\beep.mp3') # NOTE playsound had to be downgraded there seems to be an issue with the latest version
    task = db.get_task(task_id)
    name = task["name"]
    va.say(f"This task has ended")
    va.confirm_task(task_id)
     
     
