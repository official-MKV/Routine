from importlib.util import set_loader
import pyttsx3
import speech_recognition
import os 
from neuralintents import GenericAssistant
os.path.append("C:\\Users\\vemma\\Desktop\\Routine")
import task_manager


 

 

 
 
 

class Assistant:
    db = task_manager()
    def __init__(self):
        engine = pyttsx3.init() 
        voices = engine.getProperty('voices') 
        engine.setProperty('voice', voices[1].id) 
        engine.setProperty('rate', 150) 
        engine.setProperty('volume', 0.6)
        mappings={
        'routine_completed':self._routine_completed,
        'routine_failed':self._routine_failed
         }

        self.assistant = GenericAssistant('intents.json', intent_methods=mappings)
        if os.path.exists('assistant_model.h5'):
            self.assistant.load_model()
        else: 
            self.assistant.train_model()
            self.assistant.save_model()
        self.speaker = engine
        self._task_id = None

    @property
    def task_id(self):
        return self._task_id
    
    @task_id.setter
    def task_id(self,id):
        self._task_id = id 

    def confirm_task(self,task_id):
        self.say("where you able to complete the task ?")
        text = self.listen()
        self.assistant.request(text)
        self.task_id = task_id


    def say(self,text):
        self.speaker.say(text)
        self.speaker.runAndWait()
    
    def listen(self):
        try:
            with speech_recognition.Microphone() as mic: 
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)
                    text = recognizer.recognize_google(audio)
                    text = text.lower()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            self.speaker.say("I didn't get that, can you repeat")
    
    def _routine_completed(self):
        self.say("Task Completed")
        self.db.update_history(self.task_id,True)

    def _routine_failed(self):
        self.db.update_history(self.task_id,False)
