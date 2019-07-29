import pygame
from setting import Settings 
class Peashooter():
	def __init__(self,screen):
		self.screen = screen
		self.image = pygame.image.load('images/peashooter.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.left = self.screen_rect.left
		self.rect.top = self.screen_rect.centery
		self.moving_up = False	
		self.moving_down = False
		self.moving_left = False
		self.moving_right = False
		self.al_setting = Settings()
	def update(self):
		
		if self.moving_up and self.rect.y > 0: 
			self.rect.centery -= self.al_setting.plantmovingspeed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += self.al_setting.plantmovingspeed
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= self.al_setting.plantmovingspeed
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.al_setting.plantmovingspeed
	def blitme(self):
		self.screen.blit(self.image, self.rect)