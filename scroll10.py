'''Animation'''
import pygame, sys, os
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()



screen = pygame.display.set_mode((3000,2000),550,32)
pywindow = pygame.display.set_mode((800, 800))

myfont = pygame.font.SysFont("monospace", 16)



tr = "new_tree.png"
b1 = "branch1.png"
b2 = "branch2.png"
b3 = "branch3.png"
speed = 1;
gravity = 1;


back = pygame.image.load(tr).convert()
back2 = pygame.image.load(tr).convert()
bran1 = pygame.image.load(b1).convert()
bran2 = pygame.image.load(b2).convert()
bran3 = pygame.image.load(b3).convert()
squirtleImg = pygame.image.load(os.path.join("mnk1.png"))
m1=pygame.image.load(os.path.join("mnk1.png"))
m2=pygame.image.load(os.path.join("mnk2.png"))
m3=pygame.image.load(os.path.join("mnk3.png"))
m4=pygame.image.load(os.path.join("mnk4.png"))
m5=pygame.image.load(os.path.join("mnk5.png"))
m6=pygame.image.load(os.path.join("mnk6.png"))
m7=pygame.image.load(os.path.join("mnk7.png"))
currentpic=1
pic_order=1
order_count=0
sqx=230
sqy=350
y = 0
br1y=170
br2y=620
br3y=410
screenHeight = 2370
score=0
flag=0

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
    y = y + 10
    if y == screenHeight:
        y = 0
    
    screen.blit(bran1, (510,br1y))    # loading branch 1
    br1y+=10
    if br1y==screenHeight:
        br1y=0

    screen.blit(bran2, (510,br2y))    # loading branch 2
    br2y+=10
    if br2y==screenHeight:
        br2y=0    

    screen.blit(bran3, (111,br3y))    # loading branch 3
    br3y+=10
    if br3y==screenHeight:
        br3y=0
        
    if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_UP:
             #   sqy -= 30
            #if event.key == pygame.K_DOWN:
             #   sqy += 10
            if event.key == pygame.K_RIGHT:
                if sqx<530 and sqx<570:                 #if on left side
                    sqy -= 20
                    sqx += 15
                   
                else:
                    sqy-=20
            if event.key == pygame.K_LEFT:
                if sqx>230 and sqx>210:                 #if on right side
                    sqy -= 20
                    sqx -= 15
                    
                else:
                    sqy -= 20
                
    else:
        if (sqy<br1y and sqy>br1y-20 and sqx>400):      # if monkey on branch 1
           screen.blit(squirtleImg, (sqx, sqy))
           sqy+=10
           flag=1
           
        elif (sqy<br2y and sqy>br2y-20 and sqx>400):    # if monkey on branch 2
           screen.blit(squirtleImg, (sqx, sqy))
           sqy+=10
           flag=1
        elif (sqy<br3y and sqy>br3y-20 and sqx<400):    # if monkey on branch 3
           screen.blit(squirtleImg, (sqx, sqy))
           sqy+=10
           flag=1
      
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

    if currentpic==1:    
        pywindow.blit(squirtleImg, (sqx, sqy))
        squirtleImg=m1
    if currentpic==2:
        pywindow.blit(m2, (sqx, sqy))
        squirtleImg=m2
    if currentpic==3:
        pywindow.blit(m3, (sqx, sqy))
        squirtleImg=m3
    if currentpic==4:    
        pywindow.blit(m4, (sqx, sqy))
        squirtleImg=m4
    if currentpic==5:
        pywindow.blit(m5, (sqx, sqy))
        squirtleImg=m5
    if currentpic==6:
        pywindow.blit(m6, (sqx, sqy))
        squirtleImg=m6
    if currentpic==7:
        pywindow.blit(m7, (sqx, sqy))
        squirtleImg=m7
    if currentpic==7:
        currentpic=1
    else:
        currentpic+=1
        
      
    scoretext = myfont.render("Score {0}".format(score), 10, (0,0,255))
    screen.blit(scoretext, (5, 10))
            
    pywindow.blit(squirtleImg, (sqx, sqy))
    
    

    msElapsed = clock.tick(36)
    pygame.display.update()
