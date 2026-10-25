# Import necessary libraries
import os  # For interacting with the operating system
import random  # For generating random numbers

import arcade  # For game development

# Get the current directory where this script is located
current_directory = os.path.dirname(os.path.abspath(__file__))


# Define the Apple class which inherits from arcade.Sprite
class Apple(arcade.Sprite):
    # Constructor for the Apple class
    def __init__(self, game):
        # Call the parent class constructor and set the image for the sprite
        super().__init__(os.path.join(current_directory, "apple1.png"))

        # Set the size of the apple sprite
        self.width = 35
        self.height = 35

        # Randomly place the apple within the game window, avoiding the edges
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)

        # Initialize the apple's movement to be stationary
        self.change_x = 0
        self.change_y = 0
