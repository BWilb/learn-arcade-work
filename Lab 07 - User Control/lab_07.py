""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class SnowMan:
    def __init__(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color
        self.sound_three = arcade.load_sound("wind5.wav")
    def draw(self):
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y + 125,
                                  self.radius / 2,
                                  self.color)
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y + 195,
                                  self.radius / 4,
                                  self.color)
        arcade.draw_circle_filled(self.position_x - 10,
                                  self.position_y + 195,
                                  self.radius / 12,
                                  arcade.csscolor.BLACK)
        arcade.draw_circle_filled(self.position_x + 15,
                                  self.position_y + 195,
                                  self.radius / 12,
                                  arcade.csscolor.BLACK)

    def update(self):

        if self.position_x < self.radius:
            self.position_x = self.radius
            print("you have reached the edge of the screen")
            arcade.play_sound(self.sound_three)
        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            print("you have reached the edge of the screen")
            arcade.play_sound(self.sound_three)
        if self.position_y < self.radius:
            self.position_y = self.radius
            print("you have reached the edge of the screen")
            arcade.play_sound(self.sound_three)
        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius - 125
            print("you have reached the edge of the screen")
            arcade.play_sound(self.sound_three)


    def snow_change(self):
        self.color = arcade.csscolor.AQUAMARINE
    def change_again(self):
        self.color = arcade.csscolor.TURQUOISE
    def reset_color(self):
        self.color = arcade.csscolor.WHITE
class Ground:
    def __init__(self):
        self.color = arcade.csscolor.GREEN

    def draw_ground(self):
        arcade.draw_rectangle_filled(0, 0, SCREEN_HEIGHT + 1000, SCREEN_WIDTH, self.color)

    def change_color(self):
        self.color = arcade.csscolor.LIGHT_GREEN

    def change_color_again(self):
        self.color = arcade.csscolor.FOREST_GREEN

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        arcade.set_background_color(arcade.csscolor.SKY_BLUE)
        self.sound = arcade.load_sound("gully.wav")
        self.sound_two = arcade.load_sound("gmae.wav")

        self.snowman = SnowMan(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4, 100, arcade.csscolor.WHITE)
        self.myGround = Ground()
    def update(self, delta_time: float):
        self.snowman.update()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if(button == arcade.MOUSE_BUTTON_LEFT):
            self.myGround.change_color()
            arcade.play_sound(self.sound_two)
        elif(button == arcade.MOUSE_BUTTON_RIGHT):
            self.myGround.change_color_again()

    def on_key_press(self, key: int, modifiers: int):
        if(key == arcade.key.T):
            self.snowman.change_again()
            print("You set the snowman's color to aquamarine")
        elif(key == arcade.key.A):
            self.snowman.snow_change()
            print("You set the snowman's color to aquamarine")
        elif(key == arcade.key.R):
            self.snowman.reset_color()
            print("You reset the snowman's color to white")
        elif(key == arcade.key.SPACE):
            arcade.play_sound(self.sound)
        else:
            print("command wasn't read correctly")
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.snowman.position_y = y
        self.snowman.position_x = x
    def on_draw(self):
        arcade.start_render()
        self.myGround.draw_ground()
        self.snowman.draw()


def main():
    window = MyGame()
    arcade.run()


main()