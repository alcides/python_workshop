class Human(object):
    """Humans can walk, speak and sleep"""
    def __init__(self, name):
        self.name = name
        self.step = 0
    def speak(self):
        print "Hi, my name is %s" % self.name
    def walk(self):
        self.step += 1
    def sleep(self):
        pass
        

class Programmer(Human):
    def sleep(self):
        raise NotImplementedError
        

joel = Human("Joel")
joel.speak()
tiago = Programmer("Tiago")
tiago.walk()
tiago.speak()
#tiago.sleep()