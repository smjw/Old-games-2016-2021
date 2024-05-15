import pygame
pygame.init()


displayWidth=500
displayHeight=500
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Pyromancer quest!")

x=250
x_change=0
y=250
y_change=0
x2=260
x2_change=0
y2=250
y2_change=0

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

clock=pygame.time.Clock() #frames pers of movement
def gameLoop():
        x=250
        x_change=0
        y=250
        y_change=0
        x2=260
        x2_change=0
        y2=250
        y2_change=0


        gameExit=False
        while not gameExit:

                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                gameExit=True

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

                        if x>displayWidth or x<0 or x2>displayWidth or x2<0:
                                #maybe state like "hit fire u dead"
                                gameExit=True
                        if y>displayHeight or y<0 or y2>displayHeight or y2<0:
                                #maybe state like "hit fire u dead"
                                gameExit=True

                        print(event)
                x+=x_change
                y+=y_change
                x2+=x2_change
                y2+=y2_change

                gameDisplay.fill(white) #will be replaced with background
                pygame.draw.rect(gameDisplay,black,[x,y,10,10])
                pygame.draw.rect(gameDisplay,red,[x2,y2,10,10])
                #rect moves, will be replaced with sprite
        
                pygame.display.update()
                clock.tick(15) #sets 30 fps

        
gameLoop()
pygame.quit()

