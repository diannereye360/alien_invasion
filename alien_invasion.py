import sys
import pygame

from settings import Settings
from ship import Ship
#firing bullet
#from bullet import Bullet

class AlienInvasion:
    #class create pygame window and responding to user input - inc: init the game & create the game resc.
    """Overall class to manage game assets and behavior. Settings, screen, and ship instance are created"""

    def __init__(self):
        """Initialize the game, and create game resources."""

        pygame.init()

        self.settings = Settings()

        #run game in fullscreen mode
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #tells pygame to figure window size to fill screen
        self.settings.screen_width = self.screen.get_rect().width #width determine will update settings obj.
        self.settings.screen_height = self.screen.get_rect().height #height detemine will update settings obj.

        ##self.screen = pygame.display.set_mode((1200, 800)) #use before setting class set-up; creates screen size
        #helps to create an instance of setting
        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #draws the ship to the screen (1)
        self.ship = Ship(self)
        
        #Set the background color
        self.bg_color = (230, 230, 230)
        

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #create the check events method 
            self._check_events()

            #allowing continuous movement 
            self.ship.update()

            #create the update screen method 
            self._update_screen()

    #create the check events method 
    def _check_events(self):
        #watch for the keyboard and mouse events; manage movements.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                #refactoring _check_events()
                self._check_keydown_events(event)
                
            #allow continuous movement 
            elif event.type == pygame.KEYUP:
                #refactoring _check_events()
                self._check_keyup_events(event)
                

                   
    #refactoring _check_events()            
    def _check_keydown_events(self, event):
        '''respond to keypresses'''
        if event.key == pygame.K_RIGHT:
            #allow continuous movement 
            self.ship.moving_right = True
            #moving both left and right - more accurate; if both keys are held down, ship stops moving 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #pressing q to quit
        elif event.key == pygame.K_q:
            sys.exit()
    
        

    #refactoring _check_events()
    def _check_keyup_events(self, event):
        '''respond to keyreleases'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            #moving both left and right - more accurate
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

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
