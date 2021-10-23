""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MySnowMan:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

        arcade.draw_circle_filled(self.position_x,
                                  self.position_y + 50,
                                  self.radius / 2,
                                  self.color)
    def update(self):

        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
class Ground:
    def __init__(self):
        self.color = arcade.csscolor.CORNSILK
    def draw_ground(self):
        arcade.draw_rectangle_filled(0, 0, SCREEN_HEIGHT + 1000, SCREEN_WIDTH, self.color)
    def change_color(self):
        self.color = arcade.csscolor.SADDLE_BROWN
    def change_color_again(self):
        self.color = arcade.csscolor.CHOCOLATE
class Tree:
    def __init__(self, position_x, position_y, width, height, color):
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, self.color)
        arcade.draw_line(self.width, self.height / 2, 25, 25, arcade.csscolor.BROWN)



class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        arcade.set_background_color(arcade.csscolor.SKY_BLUE)
        self.tree = Tree(100, 200, 20, 20, arcade.csscolor.BROWN)
        self.snowman = MySnowMan(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 40, arcade.csscolor.WHITE)
        self.ground = Ground()

        self.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()
        self.ground.draw_ground()
        self.snowman.draw()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.snowman.position_x = x
        self.snowman.position_y = y

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.ground.change_color()
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            self.ground.change_color_again()
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snowman.position_y +=

def main():
    window = MyGame()
    arcade.run()


main()