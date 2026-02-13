class Phone:
    def make_call(self, number):
        return f"Calling {number}"

class MusicPlayer:
    def play_song(self, song):
        return f"Playing {song}"

class SmartDevice(Phone, MusicPlayer):
    pass

s1 = SmartDevice()
print( s1.make_call("123"))