'''''''''
Classe Land
'''''''''

from random import choice, randrange
from actor import Actor, Arena

class Land(Actor):

    def __init__(self, arena,x, y, w, h):
        self._x, self._y = x, y
        self._w, self._h = w, h 
        self._arena = arena
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        pass
        
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        pass
