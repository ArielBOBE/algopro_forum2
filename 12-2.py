import sys
import pygame


def run_game():
    pygame.init()
    bg_color = (0, 0, 0)
    screen = pygame.display.set_mode((1200, 800))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((255, 255, 255))
        image = pygame.image.load('images/YaeMiko2.bmp')
        screen.blit(image, (0,0))
        pygame.display.flip()


run_game()
