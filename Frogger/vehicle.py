'''''''''
Classe Vehicle
'''''''''

from random import choice, randrange
from actor import Actor, Arena

class Vehicle(Actor):

    def __init__(self, arena, x: int, y: int , direzione: int,tipo: int): # var direzione può assure due valori, o 1 o 0, e cambia la direzione in base al numero passato
        self._x, self._y = x, y
        self._w, self._h = 21, 23
        self._speed = 2
        self._direzione=direzione
        self._tipo=tipo
        self._dx = self._speed
        self._arena = arena
        arena.add(self)

    def move(self):
        if(self._direzione==0):
            arena_w, arena_h = self._arena.size()
            arena_w= arena_w + ((arena_w/100)*30)
            if not (0 <= self._x <= arena_w):
                self._x = arena_w
            self._x -= self._dx
        else:
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
        if(self._tipo==0):
            return 85, 264, self._w, self._h
        elif(self._tipo==1):
            return 74, 301, 24, self._h
        elif(self._tipo==2):
            return 47, 264, self._w, self._h
        elif(self._tipo==3):
            return 85, 264, self._w, self._h
        elif(self._tipo==4):
            return 107, 303, 46, self._h
        else:
            return 85, 264, self._w, self._h
