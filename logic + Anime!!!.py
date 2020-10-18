import pygame, sys, os, time
from pygame.locals import*

pygame.init()

GAMEWINDOW = pygame.display.set_mode((900, 700), 0, 32)
pygame.display.set_caption("DSA")

black=( 0, 0, 0)
green=( 0, 128, 0)
red=(255, 0, 0)                                      
white = (255, 255, 255)
wordColor = (153, 51, 51)
background = (51, 255, 51)
success = (26, 255, 255)

up = pygame.image.load('up.png')
down = pygame.image.load('down.png')
pause = pygame.image.load('pause.png')
resume = pygame.image.load('resume.png')

def terminate():
    pygame.quit()
    sys.exit()


def pr():
    pygame.draw.rect(GAMEWINDOW,background,(825, 0, 75, 75), 0)
    GAMEWINDOW.blit(pause, (830, 0))
    pygame.display.update()
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                xpos,ypos=event.pos
                if xpos>620 and ypos<80:
                    return 
def sleep():
    t_end = time.time() + 2
    flag = 1
    while time.time() < t_end:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                xpos,ypos=event.pos
                if xpos>620 and ypos<80:
                    if flag:
                        pr()
        
        pygame.display.update() 

def logic():
    
    #s = "abbaacdbcab"
    #t=  "abc"
    s = "ADOBECODEBANC"
    t = "ABC"
    window = dict()
    for i in t:
        if i in window:
            window[i]     +=1
        else:
            window[i] = 1    
    
    required = len(window)
    res = [-1, 0, 0]
    l = 0
    r = 0
    expected = 0
    minimumWindow = dict()

    def pygameGraphics():
        GAMEWINDOW.fill(background)
        # pause and resume
        GAMEWINDOW.blit(resume, (830, 0))
        
        # Success words background
        if(l<=r and expected == required):
            for i in range(l, r+1):
                pygame.draw.rect(GAMEWINDOW,success,(80+(i*40),90,40,40), 0)        
        
        # Displaying s
        obj=pygame.font.Font('freesansbold.ttf',30)
        surf=obj.render("s = ",True,(0, 32, 128))
        GAMEWINDOW.blit(surf,(30,95))
        
        obj=pygame.font.Font('freesansbold.ttf',35)
        for i in range(len(s)):
            pygame.draw.rect(GAMEWINDOW,white,(80+(i*40),90,40,40), 4)
            surf=obj.render(s[i],True,red)
            GAMEWINDOW.blit(surf,(88+(i*40),95))
            
        # Displayong t

        obj=pygame.font.Font('freesansbold.ttf',30)
        surf=obj.render("t = ",True,(0, 32, 128))
        GAMEWINDOW.blit(surf,(650,30))
        
        obj=pygame.font.Font('freesansbold.ttf',45)
        surf=obj.render(t,True,red)
        GAMEWINDOW.blit(surf,(700,20))

                
        # Displaying window

        obj=pygame.font.Font('freesansbold.ttf',30)
        surf=obj.render("Window",True,wordColor)
        GAMEWINDOW.blit(surf,(605,75))
        
        obj=pygame.font.Font('freesansbold.ttf',20)
        pygame.draw.rect(GAMEWINDOW,white,(600,110,120,40), 3)
        surf=obj.render("Character",True,white)
        GAMEWINDOW.blit(surf,(610,120))
        pygame.draw.rect(GAMEWINDOW,white,(600+120,110,120,40), 3)
        surf=obj.render("Count",True,white)
        GAMEWINDOW.blit(surf,(750,120))
        
        obj=pygame.font.Font('freesansbold.ttf',30)
        for i in range(len(t)):
            pygame.draw.rect(GAMEWINDOW,white,(600,150+(i*40),120,40), 3)
            surf=obj.render(t[i],True,red)
            GAMEWINDOW.blit(surf,(650,155+(i*40)))
            
            pygame.draw.rect(GAMEWINDOW,white,(600+120,150+(i*40),120,40), 3)
            surf=obj.render(str(window[t[i]]),True,red)
            GAMEWINDOW.blit(surf,(650+120,155+(i*40)))             

        # Displaying  minimum window

        obj=pygame.font.Font('freesansbold.ttf',30)
        surf=obj.render("Minimum Window",True,wordColor)
        GAMEWINDOW.blit(surf,(600,320))
        
        obj=pygame.font.Font('freesansbold.ttf',20)
        
        pygame.draw.rect(GAMEWINDOW,white,(600,350,120,40), 3)
        surf=obj.render("Character",True,white)
        GAMEWINDOW.blit(surf,(610,360))
        
        pygame.draw.rect(GAMEWINDOW,white,(600+120,350,120,40), 3)
        surf=obj.render("Count",True,white)
        GAMEWINDOW.blit(surf,(750,360))

        obj=pygame.font.Font('freesansbold.ttf',30)
        i=0
        for j in minimumWindow:
            pygame.draw.rect(GAMEWINDOW,white,(600,390+(i*40),120,40), 3)
            surf=obj.render(j,True,red)
            GAMEWINDOW.blit(surf,(650,395+(i*40)))
            
            pygame.draw.rect(GAMEWINDOW,white,(600+120,390+(i*40),120,40), 3)
            surf=obj.render(str(minimumWindow[j]),True,red)
            GAMEWINDOW.blit(surf,(650+120,395+(i*40)))

            i+=1

        # Displaying left and right with arrows

        GAMEWINDOW.blit(up, (75+40*l, 143))
        GAMEWINDOW.blit(down, (75+40*r, 28))

        # Displaying Results:
        if res[0]!=-1:
            smallest_so_far = s[res[1] : res[2]+1]
            smallest_length = str(res[0])
        else:
            smallest_so_far = " - "
            smallest_length = '0'
            
        obj=pygame.font.Font('freesansbold.ttf',25)
        
        surf=obj.render("Result: ",True,white)
        GAMEWINDOW.blit(surf,(80,300))

        surf=obj.render("Smallest substring length: " + smallest_length,True,black)
        GAMEWINDOW.blit(surf,(80,330))
        
        surf=obj.render("Smallest subtring so far: " + smallest_so_far,True,black)
        GAMEWINDOW.blit(surf,(80,360))

        surf=obj.render("Left: " + str(l),True,black)
        GAMEWINDOW.blit(surf,(80,390))

        surf=obj.render("Right: " + str(r),True,black)
        GAMEWINDOW.blit(surf,(80,420))
        

    
    pygameGraphics()
           
    ### LOGIC!!!
    while r < len(s):
        c = s[r]
        if c in minimumWindow:
            minimumWindow[c] += 1
        else:
            minimumWindow[c] = 1
        pygameGraphics()
        pygame.display.update()            
        if (c in window) and (window[c] == minimumWindow[c]):
            expected += 1    
        while (l <= r) and (expected == required):
            if res[0] == -1 or (res[0] > (r-l)+1):
                res[0] = (r-l) + 1
                res[1] = l
                res[2] = r
            pygameGraphics()
            pygame.display.update()
            sleep()
            c = s[l]
            minimumWindow[c] -= 1
            l += 1
            if(c in window) and (minimumWindow[c] < window[c]):
                expected -= 1
                pygameGraphics()
                pygame.display.update()
            
        r += 1
        sleep()
       
    if res[0] == -1:
        answer = "No match found"
    else:
        answer = s[res[1]:res[2]+1]

    obj=pygame.font.Font('freesansbold.ttf',25)
    surf=obj.render("Minimum Window Substring is: ",True,black)
    GAMEWINDOW.blit(surf,(100,515))
    obj=pygame.font.Font('freesansbold.ttf',35)
    surf=obj.render(answer,True,(0, 32, 128))
    GAMEWINDOW.blit(surf,(480,510)) 
    while(1):
        sleep()


logic()
    




    
