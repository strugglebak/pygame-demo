import pygame
import random

class Enemy:
	def __init__(self, img_name):
		self.x = 200
		self.y = -50
		self.speed = 0.3
		self.image = pygame.image.load(img_name).convert_alpha()

	def restart(self):
		self.x = random.randint(50, 400)
		self.y = random.randint(-200, -50)
		self.speed = random.random() + 0.1

	def move(self):
		if self.y < 800:
			self.y += self.speed
		else:
			self.restart()

