import time # importing functionality
import random
import pygame

pygame.init()
pygame.font.init()

displayWidth=1000 # setting the window for the game
displayHeight=700
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Pyromancer quest!")
gameFont= pygame.font.SysFont(None, 30)

white = (255,255,255) # defining the colours i will be using in the game
black = (0,0,0)#                as variables for easier use
red = (255,0,0)
blue=(0,0,255)
purple=(250,0,250)

background = pygame.image.load("field.png")

clock=pygame.time.Clock() #frames pers of movement
        
def gameLoop():
        pauseMenu=False 
#variables listed in this section
        x=displayWidth/2
        x_change=0
        y=displayHeight/2
        y_change=0

        x2=displayWidth/2 +10
        x2_change=0
        y2=displayHeight/2
        y2_change=0

        x3=100
        y3=100
        x4=200
        y4=200
        
        w=30
        h=30
        w2=30
        h2=30
        r=30
        fps=15

        score= 1000
        gem=0
        
#randomises the initial position of the gems
        ranGemX=round(random.randrange(20,displayWidth-20)/10)*10
        ranGemY=round(random.randrange(20,displayHeight-20)/10)*10

        gameExit=False
        while not gameExit:

                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                gameExit=True # closes game when cross is clicked

                        if event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_p:
                                        pauseMenu=True

                        while pauseMenu==True:
                                print("pause menu works")
                                img=gameFont.render('hello',True,white)
                                gameDisplay.blit(img,(100,100))
                                for event in pygame.event.get():
                                        if event.type==pygame.KEYDOWN:
                                                if event.key==pygame.K_p:
                                                        pauseMenu=False

                        if event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_LEFT:# first character
                                        x_change=-10 #moves by 10 for each key press
                                elif event.key==pygame.K_RIGHT:
                                        x_change=10
                                elif event.key==pygame.K_UP:
                                        y_change=-10
                                elif event.key==pygame.K_DOWN:
                                        y_change=10
                                if event.key==pygame.K_a:#second character
                                        x2_change=-10 
                                elif event.key==pygame.K_d:
                                        x2_change=10
                                elif event.key==pygame.K_w:
                                        y2_change=-10
                                elif event.key==pygame.K_s:
                                        y2_change=10

                        if event.type==pygame.KEYUP:
                                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                                        x_change=0
                                elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                                        y_change=0
                                if event.key==pygame.K_a or event.key==pygame.K_d:
                                        x2_change=0
                                elif event.key==pygame.K_w or event.key==pygame.K_s:
                                        y2_change=0

#when out of bounds of map the game closes
                        if x>displayWidth or x<0 or x2>displayWidth or x2<0:
                                gameExit=True
                        
                        if y>displayHeight or y<0 or y2>displayHeight or y2<0:
                                gameExit=True

#makes the enemies chase the player
                        while x3!=x and y3!=y:
                                if x3>x:
                                        x3=x3-1
                                else:
                                        x3=x3+1
                                if y3>y:
                                        y3=y3-1
                                else:
                                        y3=y3+1

                        while x4!=x2 and y4!=y2:
                                if x4>x2:
                                        x4=x4-1
                                else:
                                        x4=x4+1
                                if y4>y2:
                                        y4=y4-1
                                else:
                                        y4=y4+1
                                
                        #print(event)
                x+=x_change
                y+=y_change
                x2+=x2_change
                y2+=y2_change
                
# this places every thing onto the pygame window
                gameDisplay.fill(white) 
                gameDisplay.blit(background,[0,0])
                pygame.draw.rect(gameDisplay,blue,[x,y,w,h])
                pygame.draw.rect(gameDisplay,red,[x2,y2,w2,h2])
                pygame.draw.rect(gameDisplay,purple,[ranGemX,ranGemY,20,20])
                pygame.draw.circle(gameDisplay,black,[x3,y3], r)
                pygame.draw.circle(gameDisplay,black,[x4,y4], r)                        
                        
# recognises the collisions between players, gems and enemies
# also changes score depending on collisions
                if x==ranGemX and y==ranGemY or x2==ranGemX and y2==ranGemY:
                                           print(" gem collide")
                                           ranGemX=round(random.randrange(20,displayWidth-20)/10)*10
                                           ranGemY=round(random.randrange(20,displayHeight-20)/10)*10
                                           score=score +10
                                           print(score)
                                           gem=gem+1
                if (x==x3 and y==y3 or x==x4 and y==y4) or (x2==x3 and y2==y3 or x2==x4 and y2==y4) :
                        score=score-10
                        print("enemy collide")
                        print(score)
                        if score<0:
                                score==0
                        
                        

                pygame.display.update()
                clock.tick(fps) #sets 30 fps


        
gameLoop() #runs the game loop
pygame.quit()      
