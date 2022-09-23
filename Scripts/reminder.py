from ast import If
import time
import argparse
import sys
import json
sys.path.append('C:\\Users\\vemma\\Desktop\\Routine') ## TODO: fix this
from task_manager import Manager
 
# Get task id
# Get task details from database/file 
# Ring an alarm
# Announce to user 

if __name__=="__main__":
    task_id = sys.argv[1]
    db = Manager()
    task = db.get_task(task_id)
    print(task)
    time.sleep(30)
