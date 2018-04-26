#-*- coding = utf-8 -*-

import pygame 
from pygame.locals import *

#config area
pygame.init()

SCREEN = pygame.display.set_mode((640,480),0)

#set game caption
pygame.display.set_caption("hello World")


#graphic render
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

pygame.draw.polygon(SCREEN, RED, ((146,0),(290,100),(36,277),(55,200),(0,106)),2)
pygame.draw.line(SCREEN, BLUE, (11,33), (55,300), 1)
pygame.draw.circle(SCREEN, GREEN, (300,50), 100, 0)
pygame.draw.ellipse(SCREEN, RED, (300,250,180,80), 1)
pygame.draw.rect(SCREEN, RED, (200,150,100,100), 1)


#draw Image
bosix = 100
bosiy = 100
bosiImg = pygame.image.load("./reimu.jpg")
SCREEN.blit(bosiImg,(bosix,bosiy))
mouseCursor = pygame.image.load('./cursor.png').convert_alpha()

#fill text
fobj = pygame.font.SysFont("comicsansms",40)
textobj = fobj.render('hello world',True,GREEN)
text = textobj.get_rect()
text.center = (400,400)
SCREEN.blit(textobj,text)


#mainloop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    x,y = pygame.mouse.get_pos()
    x-= mouseCursor.get_width()/2
    y-= mouseCursor.get_height()/2
    SCREEN.blit(mouseCursor,(x,y))
    pygame.display.update()

