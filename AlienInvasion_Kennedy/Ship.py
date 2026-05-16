""" python programming
Alien Invasion Game
I will be modifying an Alien Game
Starter Code: Original Starter Rep from:
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: May 14 2026 """

from pathlib import Path
import pygame


class Ship:
    """Classinf ship for the players"""

    def __init__(self, ai_game):
        """Get in Position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Create path to ship
        base_path = Path(__file__).resolve().parent
        ship_path = base_path / "images" / "ship2"

        # Loading the ship image
        self.image = pygame.image.load(ship_path)

        #turns the ship to face right
        self.image = pygame.transform.rotate(self.image, -90)

        self.rect = self.image.get_rect()

        # Start ship on left side
        self.rect.midleft = self.screen_rect.midleft

        # Store decimal values for smooth movement
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Change the ship's position based on movement flags."""

        # Move ship up
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Move ship down
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update object from self.y
        self.rect.y = self.y

    def center_ship(self):
        """Center the ship on the left side of the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

        BASE_DIR = Path(__file__).reslove().parent
        image_path = BASE_DIR / "images" / "custom_ship.png"