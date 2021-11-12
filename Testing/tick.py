import arcade
import random
WIDTH = 60
HEIGHT = 60
MARGIN = 5
COLUMN_COUNT = 10
ROW_COUNT = 10
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        self.color = arcade.csscolor.GREEN

        arcade.set_background_color(arcade.color.BLACK)

        """Creation of grid of numbers"""
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)
        self.grid[1][1] = 1
        self.grid[0][2] = 1
        self.grid[0][3] = 1

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = MARGIN + WIDTH / 2 + column * (WIDTH + MARGIN)
                y = MARGIN + HEIGHT / 2 + row * (HEIGHT + MARGIN)
                if self.grid[row][column] == 0:
                    self.color = (random.randrange(256),
                                  random.randrange(256))
                else:
                    self.color = arcade.csscolor.GREEN
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, self.color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            column = x // (WIDTH + MARGIN)
            row = y // (HEIGHT + MARGIN)

            print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        if row < ROW_COUNT and column < COLUMN_COUNT:
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0




def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()