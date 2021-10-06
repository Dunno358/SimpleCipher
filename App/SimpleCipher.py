import pygame
from pygame import rect
from pygame.locals import *
import os
from datetime import datetime
from random import randint
from random import uniform
import sys
import os
import time
pygInit = pygame.init()
pygame.key.set_repeat(500, 100)
print("\nPygame init: {}/7 Succed and {} failed".format(pygInit[0],pygInit[1]))
print("Init_Start_Time: ",str(datetime.now())[10:])

dirPath = os.path.dirname(os.path.realpath(__file__))
dirPath = dirPath[:-4] #-14 for .exe, -4 for .py
print("Dir Path: ",dirPath)

name = "SimpleCipher"

displaySize = pygame.display.Info()
size_w_minus = displaySize.current_w//91
size_h_minus = displaySize.current_h//10
size_w=displaySize.current_w
size_h=displaySize.current_h

size_w = int(size_w/1.70)
size_h = int(size_h/1.28)

size=[size_w,size_h]

class Write(pygame.sprite.Sprite):
    def __init__(self,size,text,color,center):
        pygame.sprite.Sprite.__init__(self)
        self.textObject = pygame.font.Font(r"{}\Fonts\TrajanPro\TrajanPro-Regular.ttf".format(dirPath),size)
        self.writeText = self.textObject.render(str(text),True,color)
        self.textRect = self.writeText.get_rect()
        self.textRect.center = center
        self.surface = screen.blit(self.writeText,self.textRect)
    def get_rect(self):
        return self.surface
class WriteItalic(pygame.sprite.Sprite):
    def __init__(self,size,text,color,center):
        pygame.sprite.Sprite.__init__(self)
        self.textObject = pygame.font.SysFont("Arial", size, bold=True, italic=True)
        self.writeText = self.textObject.render(str(text),True,color)
        self.textRect = self.writeText.get_rect()
        self.textRect.center = center
        self.surface = screen.blit(self.writeText,self.textRect)
    def get_rect(self):
        return self.surface
class CustomRect(pygame.sprite.Sprite):
    def __init__(self,surface,location):
        pygame.sprite.Sprite.__init__(self)
        self.imageRect = surface
        self.rect = self.imageRect.get_rect()
        self.rect.left, self.rect.top = location
        self.surface = screen.blit(self.imageRect,self.rect)
    def get_rect(self):
        return self.surface

class Start():
    def author():
        authorComm = Write(10,"Made by Mariusz Walczyk",start.color("blue"),[720,10])
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
    def init():
        global size, screen, background,name
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption(name)

        background = pygame.image.load(r"{}\Pictures\main2-922x674.jpg".format(dirPath))
        screen.blit(background, (0,0)) 
        pygame.display.flip()
    def chooseAction():
        optImg = pygame.image.load(r"{}\Pictures\mainoptrect-300x70.jpg".format(dirPath))
        optImg = pygame.transform.scale(optImg, [int(size_w/2.75),int(size_h/8.8)])
        
        opt1 = CustomRect(optImg,[size_w/3.2,size_h/3.31])
        opt1R = opt1.get_rect()
        optRect1 = pygame.draw.rect(screen, start.color('purple'),[size_w/3.2,size_h/3.31,opt1R[2],opt1R[3]],size_w//120)
        Write(48,"Cipher",start.color("black"),[size_w/2.02,size_h/2.72])

        opt2 = CustomRect(optImg,[size_w/3.2,size_h/2.14])
        opt2R = opt2.get_rect()
        optRect1 = pygame.draw.rect(screen, start.color('purple'),[size_w/3.2,size_h/2.14,opt1R[2],opt1R[3]],size_w//120)
        Write(48,"Decipher",start.color("black"),[size_w/2.02,size_h/1.89])
    def quit():
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
class Admin():
    def counterCords():
        bckgr = pygame.draw.rect(screen, start.color('white'), [size_w-size_w//10,size_h-size_h//10,size_w//8,size_h//12], 0) 
        try:     
            Write(round(size_w//100*1.5),"size_w/{}".format(round(size_w/mouse_pos[0],2)),start.color('black'),[size_w-size_w//20,size_h-size_h//12])   
            Write(round(size_w//100*1.5),"size_h/:{}".format(round(size_h/mouse_pos[1],2)),start.color('black'),[size_w-size_w//20,size_h-size_h//20])  
        except:
            pass 

statement = True
start = Start
admin = Admin

start.init()
start.author()
while statement:
    try:
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos() 
    except:
        pass
    admin.counterCords()
    start.chooseAction()
    start.quit()
    pygame.display.update()
