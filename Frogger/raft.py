'''''''''
Classe Raft
'''''''''

from random import choice, randrange
from actor import Actor, Arena

class Raft(Actor):

    def __init__(self, arena, x: int, y: int, tipo: int):
        self._x, self._y = x, y
        if(tipo==0):
            self._w, self._h = 176, 20
        elif(tipo==1):
            self._w, self._h = 115, 20
        else:
            self._w, self._h = 80, 20
        self._speed = 1
        self._dx = self._speed
        self._tipo=tipo
        self._arena = arena
        arena.add(self)

    def move(self):
            arena_w, arena_h = self._arena.size()
            arena_w= arena_w + ((arena_w/100)*30)
            if not (0-((arena_w/100)*30) <= self._x <= arena_w):
                self._x = arena_w
            self._x -= self._dx

    def collide(self, other):
        pass
        
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if(self._tipo==0):
            return 7, 166, 176, 20
        elif(self._tipo==1):
            return 7, 197, 115, 20
        else:
            return 7, 231, 80, 20
        
    def getspeed(self):
        return self._speed
