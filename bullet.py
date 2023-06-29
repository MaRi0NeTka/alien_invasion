import pygame
from pygame.sprite import Group, Sprite

class Bullet(Sprite):
    """class for control bullet"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        """bullet in position (0, 0) and similar position like ship"""
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        '''позиция снаряда хранится в вещественном формате'''
        self.y = float(self.rect.y)

    def update(self):
        '''moving bullet'''
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        '''showing a bullet'''
        pygame.draw.rect(self.screen, self.color, self.rect)