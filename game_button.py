def game_button(message, x, y, width, height, active_color, inactive_color, action = None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if ((x + width > mouse[0] > x) and (y + height > mouse[1] > y)):
		pygame.draw.rect(game_display, active_color, (x, y, width, height))
		if ((click[0] == 1) and (action != None)):
			action()

	else:
		pygame.draw.rect(game_display, inactive_color, (x, y, width, height))

	text = pygame.font.SysFont(None, 20)
	# text_surf, text_rect = text_objects(message, text)
	text_surf = font.render(message, message)
	text_rect = text_surf.get_rect()
	text_rect.center = ( (x + width / 2), (y + height / 2) )
	game_display.blit(text_surf, text_rect)
