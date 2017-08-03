# -*- coding:utf-8 -*-
import pygame
from sys import exit

picSelect = 0

pygame.init()

# create a window, and the window's size is the same as the picture
screen = pygame.display.set_mode((600, 300), 0, 32)

pygame.display.set_caption("hello, World!")

background = pygame.image.load('bg.jpg').convert()
plane = pygame.image.load('plane.jpg').convert()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		screen.blit(background, (0, 0))

		(x, y) = pygame.mouse.get_pos()
		x -= plane.get_width() / 2
		y -= plane.get_height() / 2

		screen.blit(plane, (x, y))
		pygame.display.update()



	


