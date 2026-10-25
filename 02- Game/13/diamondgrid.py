# todo
import arcade


class DiamondGrid(arcade.Window):
    def __init__(self):
        # Initialize the window with a title and set dimensions
        super().__init__(width=400, height=400, title="Diamond Grid")
        # Define the properties of the diamonds
        self.diamond_size = 15
        self.spacing = 8
        # Define colors for the diamonds
        self.colors = {"primary": arcade.color.RED, "secondary": arcade.color.BLUE}
        # Set the background color of the window
        arcade.set_background_color(arcade.color.FLORAL_WHITE)

    def draw_diamond(self, x, y, size, color):
        # Calculate the vertices of the diamond shape
        half_size = size / 2
        points = [(x - half_size, y), (x, y + half_size), (x + half_size, y), (x, y - half_size)]
        # Draw the diamond shape with the given color
        arcade.draw_polygon_filled(points, color)

    def on_draw(self):
        # Start rendering the window
        arcade.start_render()
        # Loop through the grid and draw diamonds
        for row in range(0, self.width, self.diamond_size + self.spacing):
            for col in range(0, self.height, self.diamond_size + self.spacing):
                # Determine the color of the diamond based on its position
                color_key = (
                    "primary"
                    if (row // (self.diamond_size + self.spacing)) % 2
                    == (col // (self.diamond_size + self.spacing)) % 2
                    else "secondary"
                )
                # Draw the diamond at the calculated position
                self.draw_diamond(
                    row + self.diamond_size / 2,
                    col + self.diamond_size / 2,
                    self.diamond_size,
                    self.colors[color_key],
                )


# Create an instance of the DiamondGrid and run the application
diamond_grid = DiamondGrid()
arcade.run()
