
import pygame
from pygame.locals import *
import os
import subprocess

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path[:-4]#-16 in .exe|-4 in .py

class Write(pygame.sprite.Sprite):
    def __init__(self,size,text,color,center):
        pygame.sprite.Sprite.__init__(self)
        self.textObject = pygame.font.Font(r"C:\SimpleCipher\Data\Fonts\TrajanPro\TrajanPro-Regular.ttf",size)
        self.writeText = self.textObject.render(text,True,color)
        self.textRect = self.writeText.get_rect()
        self.textRect.center = center
class CustomRect(pygame.sprite.Sprite):
    def __init__(self,image,location):
        pygame.sprite.Sprite.__init__(self)
        self.imageRect = pygame.image.load(image).convert()
        self.rect = self.imageRect.get_rect()
        self.rect.left, self.rect.top = location
def author():
    authorComm = Write(10,"Made by Mariusz Walczyk",color("blue"),[720,10])
    screen.blit(authorComm.writeText,authorComm.textRect)
    pygame.display.update()
def color(colorString):
    global colorList
    colorList = {
        "green" : (0,255,0),
        "purple" : (100,15,161),
        "lt_blue" : (150,255,255),
        "blue" : (81,132,184),
        "dark_blue" : (50,50,250),
        "red" : (225,0,0),
        "white" : (255,255,255),
        "black" : (0,0,0),
        "lt_purple" : (127,0,255),
        "gray" : (169,169,169),
        "dark_green" : (0,71,49)
    } 
    return colorList[str(colorString)]
def startCheck():
    pygame.init()
    success, failure = pygame.init()
    print("Pygame-InitStatus: {0} successes and {1} failures.".format(success, failure))
    global name
    name = "SimpleCipher"
    print("Application-Status({0}): Starting...".format(name))
    print("Application-Status({0}): Started".format(name))
def mainPage():
    global size, screen, background
    size = s1,s2 = (800,600)
    screen = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption(name)

    background = pygame.image.load(r"C:\SimpleCipher\Data\Pictures\main2-922x674.jpg")
    screen.blit(background, (0,0))

    optionRect1 = CustomRect(r"C:\SimpleCipher\Data\Pictures\mainoptrect-300x70.jpg",[250,180])
    optionRect1_text = Write(48,"Cipher",color("black"),[390,220])
    screen.blit(optionRect1.imageRect,optionRect1.rect)
    screen.blit(optionRect1_text.writeText,optionRect1_text.textRect)

    optionRect2 = CustomRect(r"C:\SimpleCipher\Data\Pictures\mainoptrect-300x70.jpg",[250,280])
    optionRect2_text = Write(48,"Decipher",color("black"),[390,320])
    screen.blit(optionRect2.imageRect,optionRect2.rect)
    screen.blit(optionRect2_text.writeText,optionRect2_text.textRect)
    
    pygame.display.flip()
def mainPageBorder1(color):
    global border1
    border1 = pygame.draw.rect(screen,color,[250,180,300,70],6)
    pygame.display.update()
def mainPageBorder2(color):
    global border2
    border2 = pygame.draw.rect(screen,color,[250,280,300,70],6)
    pygame.display.update()



#Start code
startCheck()
mainPage()
mainPageBorder1(color("purple"))
mainPageBorder2(color("purple"))
author()


#events handling
statement = True

while statement:
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        #QUIT
        if event.type == QUIT:
            pygame.quit()
            quit()
            statement = False
        elif event.type == pygame.MOUSEMOTION:
            #Coords
            cipherBackButton = mouse_pos[0] in list(range(0,36)) and mouse_pos[1] in list(range(0, 31))
            #Border color change on mouseover - mainPage
            if border1.collidepoint(mouse_pos):
                mainPageBorder1(color("lt_purple"))
            else:
                mainPageBorder1(color("purple"))
            if border2.collidepoint(mouse_pos):
                mainPageBorder2(color("lt_purple"))
            else:
                mainPageBorder2(color("purple"))
            #Cipher Page color events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and border1.collidepoint(mouse_pos): #goto cipher
                pygame.quit()
                os.system(r"{}Data\dist\SimpleCipher-Cipher\SimpleCipher-Cipher.exe".format(dir_path))
                exit()
            elif event.button == 1 and border2.collidepoint(mouse_pos): #goto decipher
                pygame.quit()
                os.system(r"C:\SimpleCipher\Data\dist\SimpleCipher-Decipher\SimpleCipher-Decipher.exe")
                exit()