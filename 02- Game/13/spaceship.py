import random

import arcade

# Constants for screen dimensions and game settings
SCREEN_WIDTH, SCREEN_HEIGHT = arcade.get_display_size()
WINDOW_WIDTH = SCREEN_WIDTH // 2
WINDOW_HEIGHT = SCREEN_HEIGHT - 100
ENEMY_SPAWN_INTERVAL = 6  # Time in seconds between enemy spawns
ENEMY_SPAWN_COUNT = 3  # Number of enemies to spawn at once


# Spaceship class representing the player's ship
class Spaceship(arcade.Sprite):
    def __init__(self, image_path, scale=1):
        super().__init__(image_path, scale)
        self.center_x = WINDOW_WIDTH // 2  # Start in the middle of the screen
        self.center_y = 100  # Start 100 pixels from the bottom
        self.speed = 5  # Speed of the spaceship
        self.change_x = 0  # Movement direction (left/right)

    def update(self):
        # Move the spaceship left or right based on current velocity
        self.center_x += self.change_x


# Enemy class representing the enemy ships
class Enemy(arcade.Sprite):
    def __init__(self, image_path, scale=1):
        super().__init__(image_path, scale)
        self.angle = 180  # Rotate the enemy to face downwards
        self.center_x = random.randint(0, WINDOW_WIDTH)  # Random start position
        self.center_y = SCREEN_HEIGHT  # Start off the top of the screen
        self.speed_y = -random.uniform(3, 8)  # Random downward speed

    def update(self):
        # Move the enemy down the screen
        self.center_y += self.speed_y


# Main game class
class Game(arcade.Window):
    def __init__(self):
        # Initialize the game window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "SpaceShip 2024")
        self.set_location((SCREEN_WIDTH - WINDOW_WIDTH) // 2, (SCREEN_HEIGHT - WINDOW_HEIGHT) // 2)
        arcade.set_background_color(arcade.color.DARK_IMPERIAL_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")

        # Create the player's spaceship
        self.player = Spaceship(":resources:images/space_shooter/playerShip1_orange.png", 0.5)
        self.enemies = arcade.SpriteList()  # List to hold all enemies
        self.enemy_spawn_timer = 0  # Timer to track enemy spawns

    def on_draw(self):
        # Render the game
        arcade.start_render()
        # Draw the background and all sprites
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.player.draw()
        self.enemies.draw()

    def on_key_press(self, symbol, modifiers):
        # Handle key presses for moving the player's ship
        if symbol == arcade.key.LEFT:
            self.player.change_x = -self.player.speed
        elif symbol == arcade.key.RIGHT:
            self.player.change_x = self.player.speed

    def on_key_release(self, symbol, modifiers):
        # Stop moving the player's ship when the keys are released
        if symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0

    def on_update(self, delta_time):
        # Update the game each frame
        self.player.update()
        self.enemies.update()

        # Check for collisions
        for enemy in self.enemies:
            if arcade.check_for_collision(self.player, enemy):
                print("Spaceship collided with an enemy!")

        # Check if it's time to spawn new enemies
        self.enemy_spawn_timer += delta_time
        if self.enemy_spawn_timer >= ENEMY_SPAWN_INTERVAL:
            self.spawn_enemies()
            self.enemy_spawn_timer = 0

    def spawn_enemies(self):
        # Spawn a set number of enemies
        for _ in range(ENEMY_SPAWN_COUNT):
            enemy = Enemy(":resources:images/space_shooter/playerShip3_orange.png", 0.5)
            self.enemies.append(enemy)


# Start the game
if __name__ == "__main__":
    window = Game()
    arcade.run()
