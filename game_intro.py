import game_button
import pygame
import game

def intro():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		game_display.fill(white_color)
		game_button("Quit", 150, 10, 500, 80, black_color, green_color, pygame.quit)
