import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        # Initialize the ship and set its starting position:
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

    # Load the ship image and get its rect:
        # pygame.image.load() returns a surface representing the ship
        # stored in self.image
        self.image = pygame.image.load('images/ship.bmp')

    # get_rect() to access the surface's rect attribute:
        # Pygame treats game elements like rectangles (rects)
        # finding the rect of both screen and object in order to match them(?)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    # Start each new ship at the bottom center of the screen:
        # work with center, centerx, or centery of a rect when centering.
        # matching the x coordinate of the ship's center to the centerx of the screen's rect
        self.rect.centerx = self.screen_rect.centerx

        # work with top, bottom, left, right when working with edge of the screen.
        # matching the y coordinate of the ship's bottom to the value of the screen rect's bottom attribute
        self.rect.bottom = self.screen_rect.bottom

        # work with x and y attributes when working with horizontal or vertical placement of rect
        # ^^^ are the x and y coordinates of its top-left corner

        # In Pygame, the origin (0, 0) is in the top-left corner of the screen, and coordinates
        # increase as you go down and to the right. On a 1200 by 800 screen, the origin is in
        # the top-left corner, and the bottom-right corner has the coordinates (1200, 800).

    # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

    # Movement flag:
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # self.rect.right returns x-coordinate value of right edge of the ship's rect
        # self.screen_rect.right is the right edge of screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        # Draw the ship at its current location
        # blit is what we use to actually display the image
        # its arguments are (image, coordinates/position)
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
