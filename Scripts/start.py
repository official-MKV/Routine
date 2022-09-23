from ast import If
import time
import argparse
import sys
from bunch import bunchify
import json
from playsound import playsound
sys.path.append('C:\\Users\\vemma\\Desktop\\Routine') ## TODO: fix this
from task_manager import Manager
import VoiceAssistant as va 
 
 

if __name__=="__main__":
    arg = sys.argv[1]
    task_id = arg[:len(arg)-1]
    playsound('C:\\Users\\vemma\\Desktop\\Routine\\Resources\\beep.mp3') # NOTE playsound had to be downgraded there seems to be an issue with the latest version
    task = bunchify(db.get_task(task_id))
    va.say(f"Time to f{task.name}")
    ## TODO
    # Recieve input to update task if necessary
     
     
