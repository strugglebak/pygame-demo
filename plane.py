import pygame

class Plane:
	def __init__(self, img_name):
		self.x = 200
		self.y = 600
		self.image = pygame.image.load(img_name).convert_alpha()

	def restart(self):
		self.x = 200
		self.y = 600

	def move(self):
		(x, y) = pygame.mouse.get_pos()
		self.x = x - self.image.get_width() / 2
		self.y = y - self.image.get_height() / 2
		