import pygame
import random

class Enemy:
	def restart(self):
		self.x = random.randint(0, 450)
		self.y = random.randint(-200, 200)
		self.speed = random.random() + 0.1

	def __init__(self, img_name):
		self.restart()
		self.image = pygame.image.load(img_name).convert_alpha()

	def move(self):
		if self.y < 800:
			self.y += self.speed
		else:
			self.restart()

