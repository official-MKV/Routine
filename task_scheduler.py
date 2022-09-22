import datetime
from tracemalloc import start
import win32com.client
from datetime import datetime as dt
from bunch import bunchify
import os
 
class TaskScheduler:
    # Default variables
    _ROOT_TASKS_ ='C:\\Windows\\System32\\Tasks' 
    _ROOT_FOLDER = 'Routine'
    _TASK_TRIGGER_DAILY = 2 # Every task added is assuemed to be daily
    def __init__(self):
        self._check_path()
        self.scheduler = win32com.client.Dispatch('Schedule.Service')
        self.scheduler.Connect()
        print((os.path.join(self._ROOT_TASKS_,self._ROOT_FOLDER)))
        self.root = self.scheduler.GetFolder(self._ROOT_FOLDER)

    def add_task(self,task):
        for i in task:
            self.create_task(bunchify(i))
        print("Done!")

    def create_task(self, task_obj):
        # print(task_obj)
        time = task_obj.time
        new_task = self.scheduler.NewTask(0)
        trigger = new_task.Triggers.Create(self._TASK_TRIGGER_DAILY)
        trigger.StartBoundary = time.isoformat()
        TASK_ACTION_EXEC = 0
        action = new_task.Actions.Create(TASK_ACTION_EXEC)
        action.ID = task_obj.id
        action.Path = 'cmd.exe'
        action.Arguments = task_obj.script
        new_task.RegistrationInfo.Description = task_obj.description
        new_task.Settings.Enabled = True
        new_task.Settings.StopIfGoingOnBatteries = False
        TASK_CREATE_OR_UPDATE = 6
        TASK_LOGON_NONE = 0
        self.root.RegisterTaskDefinition(
            task_obj.name,  # Task name
            new_task,
            TASK_CREATE_OR_UPDATE,
            '',  # No user
            '',  # No password
            TASK_LOGON_NONE
        )
    def _check_path(self):
        path = os.path.join(self._ROOT_TASKS_,self._ROOT_FOLDER)
        print( os.path.exists(path))
        if os.path.exists(path):
            print("path exists")
        else: 
            print("path does not exist")
            os.mkdir(path)
            print("path created")
        




         
       
         
    


class Task:
    starttask=''
    endtask =''
    reminder=''
    reminder_duration= 5
    def __init__(self,id,name,start_time,end_time) -> None:
        self.id =id
        self.name=name
        self.start_time=dt.combine(datetime.date.today(),start_time)
        self.end_time=dt.combine(datetime.date.today(),end_time)

    def generate_task_profile(self):
        return [
            {
                'id':self.id,
                'name':self.name+' R',
                'time':self.start_time - datetime.timedelta(minutes=self.reminder_duration),
                'script':self.reminder,
                'description':'Task Reminder'
            },
            {
                'id':self.id,
                'name':self.name+' S',
                'time':self.start_time,
                'script':self.starttask,
                'description':'Start of task'
            },
            {
                'id':self.id,
                'name':self.name + ' E',
                'time':self.end_time,
                'script':self.endtask,
                'description':'End of task'
            }
        ]