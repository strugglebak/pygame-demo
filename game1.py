# -*- coding:utf-8 -*-
import pygame
from sys import exit

picSelect = 0

pygame.init()

# create a window, and the window's size is the same as the picture
screen = pygame.display.set_mode((600, 300), 0, 32)

pygame.display.set_caption("hello, World!")

background = pygame.image.load('bg.jpg').convert()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		elif event.type == pygame.MOUSEBUTTONDOWN:
			if picSelect == 0:
				background = pygame.image.load('bg2.jpg').convert()
				picSelect = 1

			elif picSelect == 1:
				background = pygame.image.load('bg3.jpg').convert()
				picSelect = 2

			elif picSelect == 2:
				background = pygame.image.load('bg.jpg').convert()
				picSelect = 0

	screen.blit(background, (0, 0))
	pygame.display.update()
