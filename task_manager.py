import json
import datetime
import os 
class Manager:
    # default 
    database_location = f"C:\\Users\\vemma\\Desktop\\Routine\\db\\temdb.json"  ## TODO: fix the path issue
    def __init__(self):
        self._data = json.load(open(self.database_location,'r+'))
        self.active='Active'
        self.not_active='Non-active'
        self.acheived ='✔'
        self.failed='❌'
    
    def get_task(self,id):
        return self._data[id]
    
    def add_data(self,task):
        self._data[task.id]={
            'name':task.name,
            'start_time':datetime.datetime.strftime(task.start_time,'%H:%M:%S'),
            'end_time':datetime.datetime.strftime(task.end_time,'%H:%M:%S'),
            'date_created':datetime.datetime.strftime(datetime.datetime.now(),' %d-%m-%Y %H:%M:%S'),
            'state':self.not_active,
            'history':{}
        }
        self._save()

    def update_state(self,id):
        ...
    def get_task_history(self):
        ...

    def _save(self):
        json.dump(self._data,open(self.database_location,'w'))

        
    def update_history(self,id,acheived:bool):
        date = datetime.datetime.strftime(datetime.datetime.today().date(),"%d-%m-%Y")
        self._data[id]['history'][date] = self.acheived if  acheived else self.failed
        self._save()

     