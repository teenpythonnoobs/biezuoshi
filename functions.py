import sys
import pygame
def check_events(shit):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
				
			if event.key == pygame.K_DOWN:
				shit.moving_down = True
			elif event.key == pygame.K_UP:
				shit.moving_up = True
			elif event.key == pygame.K_LEFT:
				shit.moving_left = True
			elif event.key == pygame.K_RIGHT:
				shit.moving_right = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				shit.moving_up = False
			elif event.key == pygame.K_DOWN:
				shit.moving_down = False
			elif event.key == pygame.K_LEFT:
				shit.moving_left = False
			elif event.key == pygame.K_RIGHT:
				shit.moving_right = False

def update_screen(ai_settings, screen, ship):

	screen.fill(ai_settings.bg_color)
	ship.blitme()