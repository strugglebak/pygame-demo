import pygame

class Bullet:
	def __init__(self, img_name):
		self.x = 0
		self.y = 0 - 1
		self.image = pygame.image.load(img_name).convert_alpha()
		self.speed = 3
		self.active = False

	def restart(self):
		(mouse_x, mouse_y) = pygame.mouse.get_pos()
		self.x = mouse_x - self.image.get_width() / 2
		self.y = mouse_y - self.image.get_height() / 2
		self.active = True

	def move(self):
		if self.active:
			self.y -= self.speed

		if self.y < 0:
			self.active = False
			
			
