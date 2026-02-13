class Speaker:
    def speak(self, message):
        return f"Speaking: {message}"

class Scheduler:
    def schedule(self, task, time):
        return f"Scheduled {task} at {time}"

class SmartAssistant(Speaker, Scheduler):
        pass

s1 = SmartAssistant()
print( s1.speak("Hi"))