# -*- coding:utf-8 -*-
import pygame
from sys import exit

resource_url = "./src/img/"

bg_url = resource_url + "back.jpg"
plane_url = resource_url + "plane.png"
bullet_url = resource_url + "bullet.png"

screen_width = 450
screen_height = 800

bt_x = -1
bt_y = -1

start_bt_x = 0
bullet_speed = 1.25

pygame.init()

# create a window, and the window's size is the same as the picture
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
# set window title
pygame.display.set_caption("SHOOOOOOOOOOOOOOOT!!!!")

background = pygame.image.load(bg_url).convert()
# this "convert_alpha" method makes the pic transparent
plane = pygame.image.load(plane_url).convert_alpha()
bullet = pygame.image.load(bullet_url).convert_alpha()


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.blit(background, (0, 0))

	(x, y) = pygame.mouse.get_pos()
	x -= plane.get_width() / 2
	y -= plane.get_height() / 2

	if bt_x < 0 or bt_y < 0:
		bt_x = x
		bt_y = y

		start_bt_x = bt_x + 20
		bt_y = bt_y + 25

	#shot the bullet
	bt_y -= bullet_speed

	#must display bullet firstly
	screen.blit(bullet, (start_bt_x, bt_y))
	screen.blit(plane, (x, y))

	pygame.display.update()
