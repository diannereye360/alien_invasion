import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect. 
        #Treat ship as rectangle. get_rect access the ship surface's rectangle attribute.
        #Rect object can use x- and y- coordinates of the top, bottom, left, and right edges and center of the rect.
        #TO CENTER - center, centerx, or centery
        #WORKING W/ EDGES - top, bottom, left, right, midbottom, midtop, midleft, and midright 
        #COORDINATES - 0,0 top left corner origin, 
        # ie. orgin 0,0; bottom left corner 1200, 800 coordinates refer to game window not physical single
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen. 
        self.rect.midbottom = self.screen_rect.midbottom

        #movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1

        if self.moving_left:
            self.rect.x -= 1
    
    def blitme(self):
        """Draw the ship at its current location (midbottom)."""
        self.screen.blit(self.image, self.rect)
