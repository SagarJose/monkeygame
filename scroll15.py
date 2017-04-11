'''Rocks, health etc'''
import pygame, sys, os
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()



screen = pygame.display.set_mode((3000,2000),550,32)
pywindow = pygame.display.set_mode((800, 800))

myfont = pygame.font.SysFont("monospace", 16)

over1="gameover.png"

tr = "new_tree.png"
b1 = "branch1.png"
b2 = "branch2.png"
b3 = "branch3.png"
b4 = "branch4.png"
b5 = "branch5.png"
b6 = "branch6.png"
b7 = "branch7.png"
st1= "stone1.png"
st2= "stone2.png"
speed = 0;
stone_speed=5
gravity = 0.01;

over = pygame.image.load(over1).convert()

back = pygame.image.load(tr).convert()
back2 = pygame.image.load(tr).convert()
bran1 = pygame.image.load(b1).convert()
bran2 = pygame.image.load(b2).convert()
bran3 = pygame.image.load(b3).convert()
bran4 = pygame.image.load(b4).convert()
bran5 = pygame.image.load(b5).convert()
bran6 = pygame.image.load(b6).convert()
bran7 = pygame.image.load(b7).convert()
stone1= pygame.image.load(st1).convert()
stone2= pygame.image.load(st2).convert()
squirtleImg = pygame.image.load(os.path.join("mnk1.png"))

sqx=530
sqy=150
y = 0
br1y=2110
br2y=1800
br3y=1510
br4y=1205
br5y=907
br6y=550
br7y=258
stn1y=0
stn2y=0
screenHeight = 2377
score=0
health=10
flag=0
mnkpos='nowhere'

while True:
    ticks = pygame.time.get_ticks()
        
    #if speed>2:
     #   speed=1
      #  gravity=0.1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    screen.blit(back, (0,y))
    screen.blit(back2,(0,y-screenHeight))        #loading and looping tree
    y = y + 1
    if y == screenHeight:
        y = 0
    
    screen.blit(bran1, (500,br1y))    # loading branch 1
    br1y+=1
    if br1y==screenHeight:
        br1y=0

    screen.blit(bran2, (150,br2y))    # loading branch 2
    br2y+=1
    if br2y==screenHeight:
        br2y=0    

    screen.blit(bran3, (505,br3y))    # loading branch 3
    br3y+=1
    if br3y==screenHeight:
        br3y=0

    screen.blit(bran4, (160,br4y))    # loading branch 4
    br4y+=1
    if br4y==screenHeight:
        br4y=0

    screen.blit(bran5, (502,br5y))    # loading branch 5
    br5y+=1
    if br5y==screenHeight:
        br5y=0

    screen.blit(bran6, (135,br6y))    # loading branch 6
    br6y+=1
    if br6y==screenHeight:
        br6y=0

    screen.blit(bran7, (490,br5y))    # loading branch 7
    br7y+=1
    if br7y==screenHeight:
        br7y=0


    if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_UP:
             #   sqy -= 30
            #if event.key == pygame.K_DOWN:
             #   sqy += 10
            if event.key == pygame.K_RIGHT:
                if sqx<530 and sqx<570:                 #if on left side
                    if flag==1:
                        sqy -= 10
                        sqx += 15
                   
                else:
                    if flag==1:
                        sqy-=10
            if event.key == pygame.K_LEFT:
                if sqx>230 and sqx>210:                 #if on right side
                    if flag==1:
                        sqy -= 10
                        sqx -= 15
                    
                else:
                    if flag==1:
                        sqy -= 10
                
    else:
        if (sqy<br1y and sqy>br1y-20 and sqx>400):      # if monkey on branch 1
           screen.blit(squirtleImg, (sqx, sqy))
           sqy+=1
           flag=1
           mnkpos='br1'
           
        elif (sqy<br2y and sqy>br2y-20 and sqx<400):    # if monkey on branch 2
           screen.blit(squirtleImg, (sqx, sqy))
           sqy+=1
           flag=1
           mnkpos='br2'
        elif (sqy<br3y and sqy>br3y-20 and sqx>400):    # if monkey on branch 3
           screen.blit(squirtleImg, (sqx, sqy))
           sqy+=1
           flag=1
           mnkpos='br3'
        elif (sqy<br4y and sqy>br4y-20 and sqx<400):    # if monkey on branch 4
           screen.blit(squirtleImg, (sqx, sqy))
           sqy+=1
           flag=1
           mnkpos='br4'

        elif (sqy<br5y and sqy>br5y-20 and sqx>400):    # if monkey on branch 5
           screen.blit(squirtleImg, (sqx, sqy))
           sqy+=1
           flag=1
           mnkpos='br5'

        elif (sqy<br6y and sqy>br6y-20 and sqx<400):    # if monkey on branch 6
           screen.blit(squirtleImg, (sqx, sqy))
           sqy+=1
           flag=1
           mnkpos='br6'

        elif (sqy<br7y and sqy>br7y-20 and sqx>400):    # if monkey on branch 7
           screen.blit(squirtleImg, (sqx, sqy))
           sqy+=1
           flag=1
           mnkpos='br7'
        #elif (sqy>br1y or sqy<br1y-20 or sqx<400):      # if monkey not on branch 1   
           #screen.blit(squirtleImg, (sqx, sqy))
    	   #sqy = sqy + speed;
           #speed = speed + gravity;
           
        #elif (sqy>br2y or sqy<br2y-20 or sqx<400):      # if monkey not on branch 2   
         #  screen.blit(squirtleImg, (sqx, sqy))
    	  # sqy = sqy + speed;
           #speed = speed + gravity;
    	  
        else:
            screen.blit(squirtleImg, (sqx, sqy))
    	    sqy = sqy + speed;
            speed = speed + gravity;
            flag=0
            
    if flag==1:
        score+=.1

    if sqy>800:
       screen.blit(over, (200,300))
       pygame.display.update()
       pygame.time.delay(1000)
       break
    if (mnkpos=='br1'):
        screen.blit(stone1, (540, stn1y))
        stn1y+=2
        if stn1y>=800:
            stn1y=0
            mnkpos='nowhere'
    if (mnkpos=='br3'):
        screen.blit(stone1, (540, stn1y))
        stn1y+=3
        if stn1y>=800:
            stn1y=0
            mnkpos='nowhere'
    if (mnkpos=='br5'):
        screen.blit(stone1, (540, stn1y))
        stn1y+=2
        if stn1y>=800:
            stn1y=0
            mnkpos='nowhere'
    if (mnkpos=='br7'):
        screen.blit(stone1, (230, stn1y))
        stn1y+=3
        if stn1y>=800:
            stn1y=0
            mnkpos='nowhere'
        

        
    if mnkpos=='br2':
        screen.blit(stone2, (230, stn2y))
        stn2y+=3
        if stn2y>=800:
            stn2y=0
            mnkpos='nowhere'

    if mnkpos=='br4':
        screen.blit(stone2, (230, stn2y))
        stn2y+=3
        if stn2y>=800:
            stn2y=0
            mnkpos='nowhere'
    if mnkpos=='br6':
        screen.blit(stone2, (230, stn2y))
        stn2y+=3
        if stn2y>=800:
            stn2y=0
            mnkpos='nowhere'


    if sqy>stn1y-1 and sqy<=stn1y+1 and sqx>=545 and sqx<=545:
        monkpos='nowhere'
        stn1y=sqy+10
        health-=1
        
    if sqy>stn2y-1 and sqy<=stn2y+1 and sqx>=230 and sqx<=235:
        monkpos='nowhere'
        stn2y=sqy+10
        health-=1
  
    #if health==-1:
       #screen.blit(over, (200,300))
       #pygame.display.update()
       #pygame.time.delay(1000)
       #break
        
    scoretext = myfont.render("Score {0}".format(score), 10, (0,0,255))
    screen.blit(scoretext, (5, 10))
    healthtext = myfont.render("Health {0}".format(health), 10, (0,0,255))
    screen.blit(healthtext, (5, 30))           
    pywindow.blit(squirtleImg, (sqx, sqy))
    
      

    msElapsed = clock.tick(200)
    pygame.display.update()
