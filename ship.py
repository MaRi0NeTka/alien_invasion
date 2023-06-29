import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    '''class to control the ship'''
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        '''download a ship'''
        self.image = pygame.image.load('shatll.png')
        self.rect = self.image.get_rect()
        '''poyavlenie v nijnem uglu'''
        self.rect.midbottom = self.screen_rect.midbottom
        '''koordinacia ship'''
        self.x = float(self.rect.x)
        '''moving'''
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''new position'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)