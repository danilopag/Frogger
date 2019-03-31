import g2d
from random import randint
from actor import Actor, Arena
from raft import Raft
from fiume import Fiume
from frog import Frog
from vehicle import Vehicle
from turtle import Turtle
from land import Land
from crocodile import Crocodile
import pygame #Gestione audio

veicoli=[]
raft=[]
frog=[]
turtle=[]
crocodile=[]
land=[]
arena = Arena(600, 480)
logo=g2d.load_image("Frogger-logo.png")
background=g2d.load_image("frogger_bg.png")
sprite = g2d.load_image("frogger_sprites.png")
gameover=g2d.load_image("gameover.png")
win=g2d.load_image("win.png")
pygame.mixer.init()
pygame.mixer.music.load("froggeraudio.mp3")
pygame.mixer.music.play()
for i in range(0,4):
        x=randint(100,200)
        raft.append(Raft(arena,x,int((i*40)+80),0))
        raft.append(Raft(arena,x+270,int((i*40)+80),1))
        raft.append(Raft(arena,x+520,int((i*40)+80),2))
for i in range(0,4):
        if(i%2==0):
                x=randint(100,250)
                turtle.append(Turtle(arena,x,int((i*40)+100)))
                turtle.append(Turtle(arena,x+30,int((i*40)+100)))
                turtle.append(Turtle(arena,x+60,int((i*40)+100)))
                x=randint(350,480)
                turtle.append(Turtle(arena,x,int((i*40)+100)))
                turtle.append(Turtle(arena,x+30,int((i*40)+100)))
                turtle.append(Turtle(arena,x+60,int((i*40)+100)))
        else:
                x=randint(100,250)
                crocodile.append(Crocodile(arena,x,int((i*40)+100)))
                x=randint(350,480)
                crocodile.append(Crocodile(arena,x,int((i*40)+100)))                
for i in range(0,5):
    if (i%2==1):
        veicoli.append(Vehicle(arena,randint(100,280),int((i*30)+280),0,i)) #paramentro x porto in un range da 150 a 480 (+ 20% del canvas) in modo da permettere alla rana di muoversi almeno nei primi momenti di gioco
        veicoli.append(Vehicle(arena,randint(350,480),int((i*30)+280),0,i))
        veicoli.append(Vehicle(arena,randint(530,680),int((i*30)+280),0,i))
    else:
        veicoli.append(Vehicle(arena,randint(100,280),int((i*30)+280),1,i))
        veicoli.append(Vehicle(arena,randint(350,480),int((i*30)+280),1,i))
        veicoli.append(Vehicle(arena,randint(530,680),int((i*30)+280),1,i))
frog.append(Frog(arena, 250,440))
fiume = Fiume(arena,0,80)
land.append(Land(arena, 0, 0, 600, 44))
land.append(Land(arena, 0, 44, 42, 30))
land.append(Land(arena, 90, 44, 80, 30))
land.append(Land(arena, 216, 44, 80, 30))
land.append(Land(arena, 343, 44, 80, 30))
land.append(Land(arena, 472, 44, 80, 30))
land.append(Land(arena, 600, 44, 40, 30))
score=[0,0,0,0,0]
playgame=False

def update():
    global playgame
    if(frog[0].getdeath()==3):
        pygame.mixer.music.pause()
        g2d.fill_canvas((0, 0, 0))
        g2d.draw_image(gameover,(20, 10))
        g2d.draw_text_centered(("SCORE:"+str(score.count(1)*1000)), (255, 255, 255), (300,400), 45)
    elif(playgame==True):
            x,y,w,h=frog[0].position()
            if((x>43 and x <85) and (y>45 and y<70) and score[0]!=1):
               score[0]=1
               frog[0].setposition(0)
               pygame.mixer.music.play()
            elif((x>175 and x <205) and (y>45 and y<70)and score[1]!=1):
               score[1]=1
               frog[0].setposition(0)
               pygame.mixer.music.play()
            elif((x>305 and x <335) and (y>45 and y<70)and score[2]!=1):
               score[2]=1
               frog[0].setposition(0)
               pygame.mixer.music.play()
            elif((x>435 and x <475) and (y>45 and y<70)and score[3]!=1):
               score[3]=1
               frog[0].setposition(0)
               pygame.mixer.music.play()
            elif((x>560 and x <590) and (y>45 and y<70)and score[4]!=1):
               score[4]=1
               frog[0].setposition(0)
               pygame.mixer.music.play()
            if(score.count(1)==5):
                pygame.mixer.music.pause()
                g2d.fill_canvas((0, 0, 0))
                g2d.draw_image(win,(20, 10))
                g2d.draw_text_centered(("SCORE:"+str(score.count(1)*1000)), (255, 255, 255), (300,400), 45)
            else:
                frog[0].setcollideraft()
                frog[0].setcollidefiume()
                frog[0].setcollideturtle()
                frog[0].setcollidecrocodile()
                arena.move_all()
                g2d.fill_canvas((255, 255, 255))
                g2d.draw_image(background,(0, 0))
                g2d.draw_text(("SCORE:"+str(score.count(1)*1000)), (255, 0, 100), (0,0), 25)
                g2d.draw_text(("DEATHS FROG:"+str(frog[0].getdeath())), (255, 0, 100), (150,0), 25)
                g2d.draw_text(("LIFE FROG:"), (255, 0, 100), (0,465), 25)
                for i in range(0,3-frog[0].getdeath()):
                        g2d.draw_image_clip(sprite, (100+i*18,465,18,15), (14, 369, 18, 15))
                for i in range(0,15):
                        veicoli[i].move()
                for i in range(0,12):
                        raft[i].move()
                for i in range(0,12):
                        turtle[i].move()
                for i in range(0,4):
                        crocodile[i].move()
                frog[0].move()
                for a in arena.actors():
                        if a != fiume and a != land[0] and a != land[1] and a != land[2] and a != land[3] and a != land[4] and a != land[5] and a != land[6]:
                                        g2d.draw_image_clip(sprite, a.position(), a.symbol())
                    
    else:
        g2d.fill_canvas((0, 0, 0))
        g2d.draw_image(logo,(20, 10))
        g2d.draw_text_centered(("PRESS ANY KEY"), (255, 255, 255), (300,240), 25)
            
                
    
    
def keydown(code):
        global playgame
        if(playgame==True):
            if code == 'ArrowUp':
                frog[0].go_up()
            elif code == 'ArrowDown':
                frog[0].go_down()
            if code == 'ArrowLeft':
                frog[0].go_left()
            elif code == 'ArrowRight':
                frog[0].go_right()
        else:
            playgame=True
            
def keyup(code):
        frog[0].stay()
        
    
def main():
    g2d.init_canvas(arena.size())
    g2d.handle_keyboard(keydown, keyup)
    g2d.main_loop(update, 1000//30)

main() 



