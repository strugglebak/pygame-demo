import pygame

class Bullet:
	def __init__(self, img_name):
		self.x = 0
		self.y = 0 - 1
		self.image = pygame.image.load(img_name).convert_alpha()
		
	def move(self, mouse_x, mouse_y, speed):
		if self.y < 0:
			self.x = mouse_x - self.image.get_width() / 2
			self.y = mouse_y - self.image.get_height() / 2	
		else:
			self.y -= speed