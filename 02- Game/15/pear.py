# Import the necessary modules
import os  # Used to interact with the operating system
import random  # Used to generate random numbers

import arcade  # Used for game development

# Get the current directory where this script is located
current_directory = os.path.dirname(os.path.abspath(__file__))


# Define the Pear class which is a type of arcade.Sprite
class Pear(arcade.Sprite):
    # Constructor for the Pear class
    def __init__(self, game):
        # Initialize the sprite with the pear image
        super().__init__(os.path.join(current_directory, "pear.png"))

        # Set the size of the pear sprite
        self.width = 35
        self.height = 35

        # Randomly place the pear within the game window, avoiding the edges
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)

        # Initialize the pear's movement to be stationary
        self.change_x = 0
        self.change_y = 0
