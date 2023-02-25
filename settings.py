class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings. Controls game's appearance and ship's speed"""
        
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #adj. ship speed - ship speed will now move 1.5 pixels rather than 1 pixel on each pass through the loop 
        self.ship_speed = 1.5

        #add bullet setting
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        