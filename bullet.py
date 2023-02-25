#create the bullet class
import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    """create the bullet class -  a class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """create the bullet class - create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.setting.bullet_color

            #create the bullet class - create a bullet rect at (0,0) and set correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

            #create the bullet class - store the bullet's position at a decimal value
        self.y = float(self.rect.y)
    
    def update(self):
        """create the bullet class - move the bullet up the screen"""
        #create the bullet class - update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        #create the bullet class - update rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

