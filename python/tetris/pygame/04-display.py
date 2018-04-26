background_image = 'sushiplate.jpg'

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,480),RESIZABLE)
background = pygame.image.load(background_image)

fullscreen = False
screenSize = (640,480)
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
		if(event.type == KEYDOWN):
			if event.key == K_f:
				fullscreen = not fullscreen
			if fullscreen:
				screen = pygame.display.set_mode(screenSize,FULLSCREEN)
			else:
				screen = pygame.display.set_mode(screenSize,RESIZABLE)
		if event.type == VIDEORESIZE:
			screenSize = event.size
			screen = pygame.display.set_mode(screenSize,RESIZABLE)
			pygame.display.set_caption("windows has reset to"+str(event.size))			
		screen_width,screen_height = screenSize
		for y in range(0,screen_height,background.get_height()):
			for x in range(0,screen_width,background.get_width()):
				screen.blit(background,(x,y))

		pygame.display.update()
	screen.blit(background,(0,0))
	pygame.display.update()

