import pygame


class Rocket():
    def __init__(self, screen):
        self.screen = screen

        # load image
        self.image = pygame.image.load('images/ship.bmp')

        # establish starting position by using rect
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # establishing desired starting position by using rect
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # movement flags:
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False



    def blitme(self):
        # drawing the image on the surface
        self.screen.blit(self.image, self.rect)



    def check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
        if event.key == pygame.K_LEFT:
            self.moving_left = True
        if event.key == pygame.K_UP:
            self.moving_up = True
        if event.key == pygame.K_DOWN:
            self.moving_down = True

    def check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
        if event.key == pygame.K_LEFT:
            self.moving_left = False
        if event.key == pygame.K_UP:
            self.moving_up = False
        if event.key == pygame.K_DOWN:
            self.moving_down = False

    def commit_movements(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1
