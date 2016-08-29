class Stranger:
    def __init__(self,name):
        self.name = name
    def sound(self,the_sound):
        self.the_sound = the_sound
        return the_sound

callhim = Stranger("Oscar")

print callhim.name
print callhim.sound("sssss")
