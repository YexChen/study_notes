background_image = 'reimu.jpg'
import pygame
from pygame.locals import *
from random import randint

pygame.init()
screen = pygame.display.set_mode((640,480))
background = pygame.image.load(background_image)
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
	randcol = (randint(0,255),randint(0,255),randint(0,255))

	screen.set_clip(0,0,300,480)
	screen.lock()
	randpoint = (randint(0,639),randint(0,479))
	screen.set_at(randpoint,randcol)
	screen.unlock()
	
	screen.set_clip(300,0,640,480)
	screen.blit(background,(350,0))
	pygame.display.update()
