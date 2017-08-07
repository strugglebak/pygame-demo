# -*- coding:utf-8 -*-
import pygame
from bullet import Bullet
from enemy import Enemy
from plane import Plane

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

gameover = False
score = 0

def checkHit(bullet, enemy):
	if (bullet.x > enemy.x and bullet.x < (enemy.x + enemy.image.get_width())) and (
		bullet.y > enemy.y and bullet.y < (enemy.y + enemy.image.get_height())):
		enemy.restart()	#let the enemy disappear
		bullet.active = False

		return True
	return False

def checkCrash(plane, enemy):
	if (plane.x + 0.7 * plane.image.get_width() > enemy.x) and (
		plane.x + 0.3 * plane.image.get_width() < enemy.x + enemy.image.get_width()) and (
		plane.y + 0.7 * plane.image.get_height() > enemy.y) and (
		plane.y + 0.3 * plane.image.get_height() < enemy.y + enemy.image.get_height()):
		return True
	return False

pygame.init()

# create a window, and the window's size is the same as the picture
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
# set window title
pygame.display.set_caption("SHOOOOOOOOOOOOOOOT!!!!")

background = pygame.image.load(bg_url).convert()
# this "convert_alpha" method makes the pic transparent
plane = Plane(plane_url)
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

# create a font
font = pygame.font.Font(None, 32)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		if gameover and event.type == pygame.MOUSEBUTTONUP:
			# reset the game
			plane.restart()

			for t_bullet in bullet_list:
				t_bullet.restart()

			for t_enemy in enemy_list:
				t_enemy.restart()

			score = 0
			gameover = False

	screen.blit(background, (0, 0))

	if not gameover:
		internal_time -= 1
		if internal_time < 0:
			bullet_list[bullet_index].restart()
			internal_time = 70
			bullet_index = (bullet_index + 1) % bullet_num

		for t_bullet in bullet_list:
			for t_enemy in enemy_list:
				# if the bullet hit the enemy
				if (checkHit(t_bullet, t_enemy)):
					score += 2

			if t_bullet.active:
				t_bullet.move()
				screen.blit(t_bullet.image, (t_bullet.x, t_bullet.y))

		plane.move()

		screen.blit(plane.image, (plane.x, plane.y))

		for t_enemy in enemy_list:
			gameover = checkCrash(plane, t_enemy)
			t_enemy.move()
			screen.blit(t_enemy.image, (t_enemy.x, t_enemy.y))

		text = font.render("Score : %d " % score, 1, (0, 0, 0))
		screen.blit(text, (0, 0))
	else:
		text = font.render("Score : %d " % score, 1, (0, 0, 0))
		screen.blit(text, (190, 300))
	

	pygame.display.update()
