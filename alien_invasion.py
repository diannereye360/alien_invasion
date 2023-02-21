import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""

        pygame.init()

        self.settings = Settings()
        ##self.screen = pygame.display.set_mode((1200, 800)) #use before setting class set-up
        #helps to create an instance of setting
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #draws the ship to the screen (1)
        self.ship = Ship(self)

        #Set the background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #create the check events method (1)
            self._check_events()

            #create the update screen method (1)
            self._update_screen()

    #create the check events method (2)
    def _check_events(self):
        #Watch for the keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #move the ship to the right one pixel exerytime arrow key is pressed
                    self.ship.rect.x += 1
                

    #create the update screen method (2)
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        #Redraw the screen during each pass through the loop
        ##self.screen.fill(self.bg_color) #use before setting class set-up
        self.screen.fill(self.settings.bg_color)

        #draws the ship to the screen (2)
        self.ship.blitme()

         #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
