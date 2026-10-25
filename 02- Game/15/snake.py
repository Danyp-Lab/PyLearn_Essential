import arcade


class Snake(arcade.Sprite):
    # Initialize the Snake class
    def __init__(self, game):
        super().__init__()
        self.width = 28  # Set the width of the snake
        self.height = 28  # Set the height of the snake
        self.radius = 16  # Set the radius for the snake's head and body parts
        self.center_x = game.width // 2  # Start the snake in the center of the game window (X-axis)
        self.center_y = (
            game.height // 2
        )  # Start the snake in the center of the game window (Y-axis)
        self.color = arcade.color.PINE_GREEN  # Set the color of the snake
        self.change_x = 0  # Initial horizontal movement is set to 0
        self.change_y = 0  # Initial vertical movement is set to 0
        self.speed = 1.5  # Set the speed of the snake
        self.score = 0  # Initialize the score
        self.body = []  # List to store the body part locations
        self.body_colors = [
            arcade.color.RED,
            arcade.color.GREEN,
        ]  # List of colors to alternate between for the body

    # Method for when the snake eats food
    def eat(self, food):
        del food  # Remove the food object
        # Increase the score when the snake eats food (uncomment the next line to enable)
        # self.score += 1
        # print("Score:", self.score)  # Print the new score

    # Method to move the snake
    def move(self):
        # Add a new body part at the current head position
        self.body.append({"x": self.center_x, "y": self.center_y})
        # Remove the oldest body part if the body is longer than the score allows
        if len(self.body) > self.score * 4:
            self.body.pop(0)

        # Update the head position based on the current direction and speed
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    # Method to draw the snake on the screen
    def draw(self):
        # Draw the head of the snake with a green color
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)

        # Draw the body segments, alternating between red and green
        for i, part in enumerate(self.body):
            color = self.body_colors[i % 2]  # Choose the color based on the current index
            arcade.draw_circle_filled(part["x"], part["y"], self.radius, color)
