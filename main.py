import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

#Screen center
screen_center_x = 800/2
screen_center_y = 600/2

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

# Create font objects
font = pygame.font.Font(None, 50)
title_font = pygame.font.Font(None, 150)

# Create text labels for the tile, the start button and the exit button
title_text = title_font.render("COMETS", True, WHITE)
title_rect = title_text.get_rect()
title_rect.center = (screen_center_x, screen_center_y - 200)
start_text = font.render("START", True, WHITE)
start_rect = start_text.get_rect()
start_rect.center = (screen_center_x, screen_center_y - 25)
exit_text = font.render("EXIT", True, WHITE)
exit_rect = exit_text.get_rect()
exit_rect.center = (screen_center_x, screen_center_y + 25)

# Set up the event loop
running = True
selected_button = "start"  # Start with the start button selected
while running:
    # Draw the start and exit buttons on the screen
    screen.fill((0, 0, 0))
    screen.blit(title_text, title_rect)
    if selected_button == "start":
        screen.blit(font.render("START", True, RED), start_rect)
        screen.blit(exit_text, exit_rect)
    else:
        screen.blit(start_text, start_rect)
        screen.blit(font.render("EXIT", True, RED), exit_rect)
    pygame.display.flip()

    # Wait for a keyboard event
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            # Highlight the start button
            selected_button = "start"
        elif event.key == pygame.K_DOWN:
            # Highlight the exit button
            selected_button = "exit"

        if selected_button == "start":
            # If start is pressed
            if event.key == pygame.K_SPACE:
                pass
        elif selected_button == "exit":
            # If Exit is pressed
            if event.key == pygame.K_SPACE:
                break