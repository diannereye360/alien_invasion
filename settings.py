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
        self.bullets_allowed = 3 #limit num bullets - limits plater to 3 bullets

        #moving aliens right - control the speed of ea alien
        #Alien sttings
        self.alien_speed = 1.0

        #create setting for fleet directions
        self.fleet_drop_speed = 10 #controls how quickly the fleet drops down the screenea time alien reaches either edge
        #fleet_direction of 1 rep. right; -1 rep. left
        self.fleet_direction = 1
        