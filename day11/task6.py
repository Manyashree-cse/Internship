class Device:
    def __init__(self, brand):
        self.brand=brand

class VoiceControl(Device):
    def voice_activate(self):
        return "voicecontrol"

class AppControl(Device):
    def app_activate(self):
        return "appcontrol"

class SmartSpeaker(VoiceControl, AppControl):
    def __init__(self,brand):
        super().__init__(brand)
    def control_methods(self):
        return f"{self.brand} can be controlled via voice and app."

s1 = SmartSpeaker("Echo")
print( s1.control_methods())
