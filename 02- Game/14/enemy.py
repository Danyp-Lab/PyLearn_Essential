import random

import arcade


class Enemy(arcade.Sprite):
    def __init__(self, screen_width, screen_height, name):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.angle = 180
        self.position = (
            random.randint(0, screen_width),  # Random x-coordinate
            screen_height,  # Set initial y-coordinate to the top of the screen
        )
        self.size = (35, 35)
        self.name = name
        self.velocity = (
            0,  # Horizontal movement
            -random.uniform(0.5, 1),  # downward movement
        )
        self.movement_direction = None  # Simplified movement direction tracking

    def move(self):
        self.position = (
            self.position[0] + self.velocity[0],  # Update x-coordinate
            self.position[1] + self.velocity[1],  # Update y-coordinate
        )
