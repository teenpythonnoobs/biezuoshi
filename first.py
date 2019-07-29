import sys
import pygame
import functions as fts
from setting import Settings
from peashooter import Peashooter
def run_game():
	al_setteing = Settings()
	pygame.init()
	screen = pygame.display.set_mode((al_setteing.screen_width, al_setteing.screen_height))
	pygame.display.set_caption("Alien Invasion")
	al_Peashooter = Peashooter(screen)	
	while True:
		fts.check_events(al_Peashooter)
		al_Peashooter.update()
		
		fts.update_screen(al_setteing,screen,al_Peashooter)
		pygame.display.flip()
		
run_game()