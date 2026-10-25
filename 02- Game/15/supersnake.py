import os

import arcade

# Importing the necessary classes for the game objects
from apple import Apple
from pear import Pear
from poo import Poo
from snake import Snake

# Get the current directory where this script is located
current_directory = os.path.dirname(os.path.abspath(__file__))


# Define the Game class which inherits from arcade.Window
class Game(arcade.Window):
    # Constructor for the Game class
    def __init__(self):
        # Get the screen dimensions and set the window dimensions
        screen_width, screen_height = arcade.get_display_size()
        window_width = 600
        window_height = 600
        # Initialize the game window
        super().__init__(width=window_width, height=window_height, title="🐍 Super Snake 🐍 V1")
        # Set a more vibrant background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Center the game window on the screen
        window_position_x = (screen_width - window_width) // 2
        window_position_y = (screen_height - window_height) // 2
        self.set_location(window_position_x, window_position_y)

        # Create instances of the game objects
        self.food = Apple(self)
        self.pear = Pear(self)
        self.poo = Poo(self)
        self.snake = Snake(self)

        # Initialize game state variables
        self.score_text = None
        self.game_over = False
        self.game_started = False

    # Method to handle the drawing of game objects
    def on_draw(self):
        # Start the rendering process
        arcade.start_render()

        # Draw the game objects
        self.food.draw()
        self.pear.draw()
        self.poo.draw()
        self.snake.draw()

        # Display the score with the default font
        score_display = f"Score: {self.snake.score}"
        arcade.draw_text(score_display, 10, self.height - 20, arcade.color.WHITE, 14)

        # Display the game over message if the game has ended
        if self.game_over and self.game_started:
            arcade.draw_text(
                "Game Over",
                self.width // 2,
                self.height // 2,
                arcade.color.RED_ORANGE,
                40,
                bold=True,
                anchor_x="center",
            )

        # Finish the rendering process
        arcade.finish_render()

    # Method to update the game state
    def on_update(self, delta_time: float):
        # Check if the game is over
        if self.game_over:
            # Remove all objects from the game
            self.snake.kill()
            self.food.kill()
            self.pear.kill()
            self.poo.kill()
        else:
            # Move the snake
            self.snake.move()

            # Check for collisions with food items and update the score
            if arcade.check_for_collision(self.snake, self.food):
                self.snake.score += 1
                self.snake.eat(self.food)
                self.food = Apple(self)

            if arcade.check_for_collision(self.snake, self.pear):
                self.snake.score += 2
                self.snake.eat(self.pear)
                self.pear = Pear(self)

            if arcade.check_for_collision(self.snake, self.poo):
                # Start the game if it hasn't started yet
                if not self.game_started:
                    self.game_started = True
                # Decrease the score if the snake hits a poo
                self.snake.score -= 1
                self.snake.eat(self.poo)
                self.poo = Poo(self)

                # End the game if the score drops to zero or below
                if self.snake.score <= 0:
                    self.game_over = True

            # Check if the snake has hit the boundaries of the game window
            if (
                self.snake.center_x < 0
                or self.snake.center_x > self.width
                or self.snake.center_y < 0
                or self.snake.center_y > self.height
            ):
                self.game_started = True
                self.game_over = True

            # Check if the snake has collided with itself
            head = {"x": self.snake.center_x, "y": self.snake.center_y}
            for segment in self.snake.body:
                if head == segment:
                    self.game_over = True

    # Method to handle key releases
    def on_key_release(self, symbol: int, modifiers: int):
        # Update the snake's direction based on the key pressed
        if symbol == arcade.key.UP and self.snake.change_y == 0:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.DOWN and self.snake.change_y == 0:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif symbol == arcade.key.RIGHT and self.snake.change_x == 0:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol == arcade.key.LEFT and self.snake.change_x == 0:
            self.snake.change_x = -1
            self.snake.change_y = 0


# The entry point of the program
if __name__ == "__main__":
    game = Game()
    arcade.run()
