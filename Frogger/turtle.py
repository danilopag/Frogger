'''''''''
Classe Turtle
'''''''''

from random import choice, randrange
from actor import Actor, Arena

class Turtle(Actor):

    def __init__(self, arena, x: int, y: int):
        self._x, self._y = x, y
        self._w, self._h = 30, 20 
        self._speed = 1
        self._dx = self._speed
        self._arena = arena
        arena.add(self)

    def move(self):
            arena_w, arena_h = self._arena.size()
            arena_w= arena_w + ((arena_w/100)*30)
            if not (0 <= self._x <= arena_w):
                self._x = 0
            self._x += self._dx

    def collide(self, other):
        pass
        
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 16, 407, self._w, self._h

    def getspeed(self):
        return self._speed

