import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,480))

def create_scales(height):
	red_scale_surface = pygame.surface.Surface((640,height))
	green_scale_surface = pygame.surface.Surface((640,height))
	blue_scale_surface = pygame.surface.Surface((640,height))
	for x in range(640):
		c = int((x/640.)*255.)
		red = (c,0,0)
		green = (0,c,0)
		blue = (0,0,c)
		line_rect = Rect(x,0,1,height)
		pygame.draw.rect(red)

