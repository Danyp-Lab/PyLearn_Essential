import arcade
from bullet import Bullet
from enemy import Enemy
from spaceship import Spaceship


class Game(arcade.Window):
    def __init__(self):
        # Initialize the game
        screen_width, screen_height = arcade.get_display_size()
        window_width, window_height = self.calculate_window_size(screen_width, screen_height)
        super().__init__(width=window_width, height=window_height, title="SpaceShip 2024")

        # Center the window on the screen
        self.center_window(screen_width, window_height)

        # Set background color and image
        arcade.set_background_color(arcade.color.DARK_IMPERIAL_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")

        # Initialize game objects
        self.me = Spaceship(window_width, "me")
        self.enemies = arcade.SpriteList()
        self.bullets = arcade.SpriteList()

        # Initialize game state
        self.lives = 3
        self.score = 0

        # Initialize enemy spawning
        self.enemy_spawn_timer = 0
        self.enemy_spawn_interval = 3  # Spawn every 3 seconds
        self.enemy_spawn_count = 1  # Number of enemies to appear every 3 seconds

        # Load sound files
        self.shoot_sound = arcade.load_sound(":resources:sounds/laser1.wav")
        self.explode_sound = arcade.load_sound(":resources:sounds/explosion2.wav")

        self.game_over = False

    def calculate_window_size(self, screen_width, screen_height):
        window_width = screen_width // 2
        window_height = screen_height - 100
        return window_width, window_height

    def center_window(self, screen_width, screen_height):
        window_position_x = (screen_width - self.width) // 2
        window_position_y = (screen_height - self.height) // 2
        self.set_location(window_position_x, window_position_y)

    def on_draw(self):
        arcade.start_render()

        # Draw background
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)

        # Draw game objects
        self.me.draw()
        self.enemies.draw()
        self.bullets.draw()

        # Display player's score
        self.draw_score()

        # Display player's lives
        self.draw_lives()

        # Display "Game Over" if the game is over
        if self.game_over:
            self.draw_game_over()

        arcade.finish_render()

    def draw_score(self):
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, self.width - 150, 10, arcade.color.DARK_YELLOW, 18)

    def draw_lives(self):
        heart_symbol = "♥️"
        heart_spacing = 20
        heart_position_x = 10
        heart_position_y = 10
        for i in range(self.lives):
            arcade.draw_text(
                heart_symbol,
                heart_position_x + i * heart_spacing,
                heart_position_y,
                arcade.color.PERSIAN_ROSE,
                24,
            )

    def draw_game_over(self):
        arcade.draw_text(
            "Game Over",
            self.width // 2,
            self.height // 2,
            arcade.color.PERSIAN_RED,
            50,
            anchor_x="center",
        )

    def on_update(self, delta_time):
        if not self.game_over:
            # Update player's movement
            if self.me.move_left:
                self.me.center_x -= self.me.speed
            elif self.me.move_right:
                self.me.center_x += self.me.speed

            # Update enemy movement
            for enemy in self.enemies:
                enemy.move()

            # Update bullets movement
            for bullet in self.bullets:
                bullet.update()

            # Check for collisions between bullets and enemies
            for bullet in self.bullets:
                hit_list = arcade.check_for_collision_with_list(bullet, self.enemies)
                if hit_list:
                    bullet.remove_from_sprite_lists()
                    for enemy in hit_list:
                        enemy.remove_from_sprite_lists()
                        self.score += 1
                        arcade.play_sound(self.explode_sound)

                        # Check if enemies have reached the bottom of the screen
            for enemy in self.enemies:
                if enemy.top < 0:
                    enemy.remove_from_sprite_lists()
                    self.lives -= 1
                    if self.lives <= 0:
                        self.game_over = True
                        self.enemies = arcade.SpriteList()
                        self.bullets = arcade.SpriteList()
                        break

                        # Check if the player's bullets are out of the screen
            for bullet in self.bullets:
                if bullet.bottom > self.height:
                    bullet.remove_from_sprite_lists()

            # Spawn enemies
            self.enemy_spawn_timer += delta_time
            if self.enemy_spawn_timer >= self.enemy_spawn_interval:
                self.spawn_enemy()
                self.enemy_spawn_timer = 0

    def on_key_press(self, symbol: int, modifiers: int):
        if not self.game_over:
            if symbol == arcade.key.LEFT or symbol == arcade.key.A:
                self.me.move_left = True
            elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
                self.me.move_right = True
            elif symbol == arcade.key.SPACE:
                bullet = Bullet(self.me.center_x, self.me.center_y + self.me.height // 2)
                self.bullets.append(bullet)
                arcade.play_sound(self.shoot_sound)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.me.move_left = False
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.me.move_right = False

    def spawn_enemy(self):
        for _ in range(self.enemy_spawn_count):
            self.create_and_add_enemy()

    def create_and_add_enemy(self):
        enemy = Enemy(self.width, self.height, "enemy")
        self.enemies.append(enemy)


window = Game()
arcade.run()
