import sys
import pygame


def run_game():
    pygame.init()
    screen_res = (1200, 800)
    screen = pygame.display.set_mode(screen_res)
    # color blue
    bg_color = (0, 0, 255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # draws the color blue on screen
        screen.fill(bg_color)
        pygame.display.flip()


run_game()
