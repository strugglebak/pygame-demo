# -*- coding:utf-8 -*-
import pygame
from bullet import Bullet
from enemy import Enemy

from sys import exit

resource_url = "./src/img/"

bg_url = resource_url + "back.jpg"
plane_url = resource_url + "plane.png"
bullet_url = resource_url + "bullet.png"
enemy_url = resource_url + "enemy.png"

screen_width = 450
screen_height = 800

bullet_speed = 1.25
enemy_speed = 0.3

pygame.init()

# create a window, and the window's size is the same as the picture
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
# set window title
pygame.display.set_caption("SHOOOOOOOOOOOOOOOT!!!!")

background = pygame.image.load(bg_url).convert()
# this "convert_alpha" method makes the pic transparent
plane = pygame.image.load(plane_url).convert_alpha()
# bullet = pygame.image.load(bullet_url).convert_alpha()
bullet = Bullet(bullet_url)
enemy = Enemy(enemy_url)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.blit(background, (0, 0))

	(x, y) = pygame.mouse.get_pos()

	bullet.move(x, y, bullet_speed)
	# enemy.move(enemy_speed)
	enemy.move()

	x -= plane.get_width() / 2
	y -= plane.get_height() / 2

	#must display bullet firstly
	screen.blit(bullet.image, (bullet.x, bullet.y))
	screen.blit(plane, (x, y))
	screen.blit(enemy.image, (enemy.x, enemy.y))

	pygame.display.update()
