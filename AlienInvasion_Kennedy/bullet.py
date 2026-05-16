"""Python Programming
This file is for the bullet functions
Kennedy Walker
Date 5/12/2026"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init(self,ai_game):

        self.screen = ai_game
        