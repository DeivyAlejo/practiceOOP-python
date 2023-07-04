class Inhabitant():
    
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    


class Werewolf(Inhabitant):
    pass

class Fairy(Inhabitant):
    pass

class Human(Inhabitant):
    pass