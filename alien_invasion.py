import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize pygame, settings, create a screen object/surface (the window of the game)
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) # Where we draw all the game's graphical elements
    pygame.display.set_caption("Alien Invasion")

# Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

# Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

# Make a ship.
    ship = Ship(ai_settings, screen)

# Make a group to store bullets and aliens in.
    bullets = Group()
    aliens = Group()

# Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

# Set the background color
    bg_color = (230, 230, 230)

# Start the main loop for the game.
    # The surface is redrawn on every iteration of loop
    # The loop will continuously update the screen by 'pygame.display.update()'
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)
        print(len(bullets))


run_game()
