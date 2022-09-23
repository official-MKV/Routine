import os 

BASE_PATH = os.getcwd()
BAT_PATH = f"{BASE_PATH}\\BatScripts"
PYTHON_PATH="C:\\Users\\vemma\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"
SCRIPT_PATH = f"{BASE_PATH}\\Scripts"
def create_batch_file(task_id,script_type):
    with open(f"{BAT_PATH}\{task_id}.bat","w+") as file: 
        file.write(f"{PYTHON_PATH} {os.path.join(SCRIPT_PATH,script_type)} {task_id} ")
    return os.path.join(BAT_PATH,f'{task_id}.bat')