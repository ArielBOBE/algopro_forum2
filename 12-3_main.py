import sys
import pygame

from 12-3_rocket import Rocket

# Make a game that begins with a rocket in the center of the
# screen. Allow the player to move the rocket up, down, left, or right using the
# four arrow keys. Make sure the rocket never moves beyond any edge of the
# screen


def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    rocket = Rocket(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                rocket.check_keydown(event)
            elif event.type == pygame.KEYUP:
                rocket.check_keyup(event)
        rocket.commit_movements()
        screen.fill((255, 255, 255))
        rocket.blitme()
        pygame.display.flip()




start_game()
