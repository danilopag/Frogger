'''''''''
Classe Fiume
'''''''''

from random import choice, randrange
from actor import Actor, Arena

class Fiume(Actor):

    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._w, self._h = 640, 155 
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
