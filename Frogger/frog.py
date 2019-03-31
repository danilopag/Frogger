import g2d
from actor import Actor, Arena
from raft import Raft
from fiume import Fiume
from turtle import Turtle
from vehicle import Vehicle
from crocodile import Crocodile
from land import Land
from random import randint

arena = Arena(600, 480)
raft= Raft(arena,0,0,0)
turtle = Turtle(arena,0,0)
crocodile = Crocodile(arena,0,0)

class Frog(Actor):
    
    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._w, self._h = 18, 15 
        self._speed = 7
        self._dx, self._dy = 0, 0
        self._arena = arena
        self._death=0
        self._collideraft=False
        self._collidefiume=False
        self._collideturtle=False
        self._collidecrocodile=False
        arena.add(self)

    def move(self):
        if(self._collideraft==False and self._collidefiume==True):
            if not(self._death<2):
                self._arena.remove(self)
                self._death=3
            else:
                self._death=self._death +1
                self.setposition(0)
        elif((self._collideturtle==False and self._collidefiume==True)or(self._collidecrocodile==False and self._collidefiume==True) ):
            if not(self._death<2):
                self._arena.remove(self)
                self._death=3
            else:
                self._death=self._death +1
                self.setposition(0)
        if(self._collideraft==True):
            self._speed=raft.getspeed()
            self.go_left()
        elif(self._collideturtle==True or self._collidecrocodile):
            self._speed=turtle.getspeed()
            self.go_right()
        else:
            self._speed=7
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > arena_h - self._h:
            self._y = arena_h - self._h

        self._x += self._dx
        if self._x < 0 and self._collideraft == True:
            if not(self._death<2):
                self._arena.remove(self)
                self._death=3
            else:
                self._death=self._death +1
                self.setposition(0)
        elif self._x > arena_w - self._w and self._collideturtle== True:
            if not(self._death<2):
                self._arena.remove(self)
                self._death=3
            else:
                self._death=self._death +1
                self.setposition(0)
        elif self._x < 0:
            self._x = 0
        elif self._x > arena_w - self._w:
            self._x = arena_w - self._w

    def go_left(self):
        self._dx, self._dy = -self._speed, 0
        self._speed=5
        
    def go_right(self):
        self._dx, self._dy = +self._speed, 0
        self._speed=5
        
    def go_up(self):
        self._dx, self._dy = 0, -self._speed
        self._speed=5
            
    def go_down(self):
        self._dx, self._dy = 0, +self._speed
        self._speed=5
            
    def stay(self):
        self._dx, self._dy = 0, 0
        self._speed=5
        
    def collide(self, other):
        if isinstance(other, Vehicle):
            if not (self._death<2):
                self._arena.remove(self)
                self._death=3
            else:
                self._death=self._death +1
                self.setposition(0)
        if isinstance(other, Land):
            if not (self._death<2):
                self._arena.remove(self)
                self._death=3
            else:
                self._death=self._death +1
                self.setposition(0)
        if not isinstance(other,Fiume):
            self._collidefiume=False
        else:
            self._collidefiume=True
        if not isinstance(other, Raft):
            self._collideraft=False
        else:
            self._collideraft=True
        if not isinstance(other, Crocodile):
            self._collidecrocodile=False
        else:
            self._collidecrocodile=True
        if not isinstance(other, Turtle):
            self._collideturtle=False
        else:
            self._collideturtle=True
        
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 14, 369, self._w, self._h

    
    def getcollideraft(self):
        return self._collideraft
    def setcollideraft(self):
        self._collideraft= False
        
    def getcollidefiume(self):
        return self._collidefiume
    def setcollidefiume(self):
        self._collidefiume= False

    def getcollideturtle(self):
        return self._collideturtle
    def setcollideturtle(self):
        self._collideturtle= False

    def getcollidecrocodile(self):
        return self._collidecrocodile
    def setcollidecrocodile(self):
        self._collidecrocodile= False
    
    def getdeath(self):
        return self._death

    def setposition(self, tipo):
        if (tipo==0):
            self._x=250
            self._y=440           
            self.stay()
        
    
