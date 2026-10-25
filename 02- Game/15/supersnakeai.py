import os

import arcade
from apple import Apple
from pear import Pear
from poo import Poo
from snake import Snake

current_directory = os.path.dirname(os.path.abspath(__file__))


class Game(arcade.Window):
    def __init__(self):
        screen_width, screen_height = arcade.get_display_size()
        window_width = 600
        window_height = 600
        super().__init__(width=window_width, height=window_height, title="🐍 Super Snake 🐍 V1")
        arcade.set_background_color(arcade.color.KHAKI)

        window_position_x = (screen_width - window_width) // 2
        window_position_y = (screen_height - window_height) // 2
        self.set_location(window_position_x, window_position_y)

        self.food = Apple(self)
        self.pear = Pear(self)
        self.poo = Poo(self)
        self.snake = Snake(self)

        self.score_text = None
        self.game_over = False
        self.game_started = False

    def find_closest_fruit(self):
        food_distance = abs(self.food.center_x - self.snake.center_x) + abs(
            self.food.center_y - self.snake.center_y
        )
        pear_distance = abs(self.pear.center_x - self.snake.center_x) + abs(
            self.pear.center_y - self.snake.center_y
        )

        if food_distance <= pear_distance:
            return self.food
        else:
            return self.pear

    def on_draw(self):
        arcade.start_render()

        self.food.draw()
        self.pear.draw()
        self.poo.draw()
        self.snake.draw()

        score_display = f"Score: {self.snake.score}"
        arcade.draw_text(score_display, 10, self.height - 20, arcade.color.BLACK, 14)

        if self.game_over and self.game_started:
            arcade.draw_text(
                "Game Over",
                self.width // 2,
                self.height // 2,
                arcade.color.RED,
                40,
                bold=True,
                anchor_x="center",
            )

        arcade.finish_render()

    def on_update(self, delta_time: float):
        if self.game_over:
            # Clear all objects from the screen
            self.snake.kill()
            self.food.kill()
            self.pear.kill()
            self.poo.kill()
        else:
            # Move the snake towards the closest fruit
            closest_fruit = self.find_closest_fruit()
            fruit_x, fruit_y = closest_fruit.center_x, closest_fruit.center_y
            snake_x, snake_y = self.snake.center_x, self.snake.center_y

            # Calculate the direction towards the closest fruit
            dx = fruit_x - snake_x
            dy = fruit_y - snake_y

            # Normalize the direction vector
            length = (dx**2 + dy**2) ** 0.5
            if length != 0:
                dx /= length
                dy /= length

            # Set the snake's velocity towards the closest fruit
            self.snake.change_x = dx
            self.snake.change_y = dy

            # Move the snake
            self.snake.move()

            # Check for collisions and game over conditions
            if arcade.check_for_collision(self.snake, closest_fruit):
                if closest_fruit == self.food:
                    self.snake.score += 1
                    self.snake.eat(self.food)
                    self.food = Apple(self)
                elif closest_fruit == self.pear:
                    self.snake.score += 2
                    self.snake.eat(self.pear)
                    self.pear = Pear(self)

            if arcade.check_for_collision(self.snake, self.poo):
                if not self.game_started:
                    self.game_started = True
                self.snake.score -= 1
                self.snake.eat(self.poo)
                self.poo = Poo(self)

                if self.snake.score <= 0:
                    self.game_over = True

            if (
                self.snake.center_x < 0
                or self.snake.center_x > self.width
                or self.snake.center_y < 0
                or self.snake.center_y > self.height
            ):
                self.game_started = True
                self.game_over = True

            head = {"x": self.snake.center_x, "y": self.snake.center_y}
            for segment in self.snake.body:
                if head == segment:
                    self.game_over = True

    def on_key_release(self, symbol: int, modifiers: int):
        pass


if __name__ == "__main__":
    game = Game()
    arcade.run()
