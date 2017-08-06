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

internal_time = 0
bullet_index = 0

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

bullet_num = 5
bullet_list = []
for i in range(0, bullet_num):
	bullet_list.append(bullet)

enemy_num = 5
enemy_list = []
for i in range(0,enemy_num):
	enemy_list.append(enemy)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.blit(background, (0, 0))

	internal_time -= 1
	if internal_time < 0:
		bullet_list[bullet_index].restart()
		internal_time = 70
		bullet_index = (bullet_index + 1) % bullet_num

	for t_bullet in bullet_list:
		if t_bullet.active:
			t_bullet.move()
			screen.blit(t_bullet.image, (t_bullet.x, t_bullet.y))

	(x, y) = pygame.mouse.get_pos()
	x -= plane.get_width() / 2
	y -= plane.get_height() / 2

	screen.blit(plane, (x, y))

	for t_enemy in enemy_list:
		t_enemy.move()
		screen.blit(t_enemy.image, (t_enemy.x, t_enemy.y))

	pygame.display.update()
