background_image = 'sushiplate.jpg'

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480))

#show text
my_font = pygame.font.SysFont("arial",64)
text_surface = my_font.render("Pygame is cool",True,(0,0,0),(255,255,255))

#save as image
pygame.image.save(text_surface,"name.png")

background = pygame.image.load('sushiplate.jpg')

x,y = 0, (480-text_surface.get_height())/2

while True:
	for event in pygame.event.get():
		if(event.type == QUIT):
			pygame.quit()
	
	screen.blit(background,(0,0))
	x -= 2
	if x < -text_surface.get_width():
		x = 640-text_surface.get_width()
	screen.blit(text_surface,(x,y))
	pygame.display.update()

