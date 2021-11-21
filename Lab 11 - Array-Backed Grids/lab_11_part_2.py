import arcade

WIDTH = 60
HEIGHT = 60
MARGIN = 5
COLUMN_COUNT = 10
ROW_COUNT = 10
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

class MyGame(arcade.Window):
    """
    Main game
    """
    def __init__(self, width, height):
        """
        init function
        """
        super().__init__(width, height)

        self.grid = []
        for row in range(ROW_COUNT):

            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """Function that draws everything"""
        arcade.start_render()

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):

                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):
        """Mouse function"""
        column = int (x // (WIDTH + MARGIN))
        row = int (y // (HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")
        if row < ROW_COUNT and column < COLUMN_COUNT:
            if row == 0:
                if column == 0:
                    if self.grid[row][column] == 0:
                        self.grid[row][column] = 1
                        self.grid[row][column + 1] = 1
                        self.grid[row + 1][column] = 1
                    else:
                        self.grid[row][column] = 0
                        self.grid[row][column + 1] = 0
                        self.grid[row + 1][column] = 0

                elif column != (COLUMN_COUNT - 1):
                    if self.grid[row][column] == 0:
                        self.grid[row][column] = 1
                        self.grid[row][column + 1] = 1
                        self.grid[row][column - 1] = 1
                        self.grid[row + 1][column] = 1
                    else:
                        self.grid[row][column] = 0
                        self.grid[row][column + 1] = 0
                        self.grid[row][column - 1] = 0
                        self.grid[row + 1][column] = 0

                elif column == (COLUMN_COUNT - 1):
                    if self.grid[row][column] == 0:
                        self.grid[row][column] = 1
                        self.grid[row][column - 1] = 1
                        self.grid[row + 1][column] = 1
                    else:
                        self.grid[row][column] = 0
                        self.grid[row][column - 1] = 0
                        self.grid[row + 1][column] = 0

            elif row != (ROW_COUNT - 1):
                if column == 0:
                    if self.grid[row][column] == 0:
                        self.grid[row][column] = 1
                        self.grid[row][column + 1] = 1
                        self.grid[row - 1][column] = 1
                        self.grid[row + 1][column] = 1
                    else:
                        self.grid[row][column] = 0
                        self.grid[row][column + 1] = 0
                        self.grid[row + 1][column] = 0
                        self.grid[row - 1][column] = 0

                elif column != (COLUMN_COUNT - 1):
                    if self.grid[row][column] == 0:
                        self.grid[row][column] = 1
                        self.grid[row][column - 1] = 1
                        self.grid[row][column + 1] = 1
                        self.grid[row - 1][column] = 1
                        self.grid[row + 1][column] = 1
                    else:
                        self.grid[row][column] = 0
                        self.grid[row][column + 1] = 0
                        self.grid[row][column - 1] = 0
                        self.grid[row + 1][column] = 0
                        self.grid[row - 1][column] = 0

                elif column == (COLUMN_COUNT - 1):
                    if self.grid[row][column] == 0:
                        self.grid[row][column] = 1
                        self.grid[row][column - 1] = 1
                        self.grid[row - 1][column] = 1
                        self.grid[row + 1][column] = 1
                    else:
                        self.grid[row][column] = 0
                        self.grid[row][column - 1] = 0
                        self.grid[row + 1][column] = 0
                        self.grid[row - 1][column] = 0

            elif row == (ROW_COUNT - 1):
                if column == 0:
                    if self.grid[row][column] == 0:
                        self.grid[row][column] = 1
                        self.grid[row][column + 1] = 1
                        self.grid[row - 1][column] = 1
                    else:
                        self.grid[row][column] = 0
                        self.grid[row][column + 1] = 0
                        self.grid[row - 1][column] = 0

                elif column != (COLUMN_COUNT - 1):
                    if self.grid[row][column] == 0:
                        self.grid[row][column] = 1
                        self.grid[row][column - 1] = 1
                        self.grid[row][column + 1] = 1
                        self.grid[row - 1][column] = 1
                    else:
                        self.grid[row][column] = 0
                        self.grid[row][column - 1] = 0
                        self.grid[row][column + 1] = 0
                        self.grid[row - 1][column] = 0

                elif column == (COLUMN_COUNT - 1):
                    if self.grid[row][column] == 0:
                        self.grid[row][column] = 1
                        self.grid[row][column - 1] = 1
                        self.grid[row - 1][column] = 1
                    else:
                        self.grid[row][column] = 0
                        self.grid[row][column - 1] = 0
                        self.grid[row - 1][column] = 0

        count = 0
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    count += 1
        print(f"there are a total of {count} cells selected")
        print()

        continuous_count = 0
        count = 0
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    continuous_count += 1
                    count += 1
            if row <= ROW_COUNT and continuous_count > 2:
                print(f"There are {continuous_count} continuous cells selected in row {row}")
            print(f"In row {row} there are a total of {count} cells selected")
            continuous_count = 0
            count = 0
        print()

        column_count = 0
        for column in range(ROW_COUNT):
            for row in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                   column_count += 1
            print(f"In column {column} there are a total of {column_count} cells selected")
            column_count = 0
        print()

def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()