""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 4

class SnowMan:
    def __init__(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color
        self.sound_three = arcade.load_sound("wind5.wav")
        """Importing sound three into snowman object"""
    def draw(self):
        """draws snowman. Each circle created after first circle is a downsized version"""
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
            print("you have gone past the edge of the screen")
            arcade.play_sound(self.sound_three)

        if self.position_x > SCREEN_WIDTH - self.radius:
            print("you have gone past the edge of the screen")
            arcade.play_sound(self.sound_three)

        if self.position_y < self.radius:
            arcade.play_sound(self.sound_three)
            print("you have gone past the edge of the screen")

        if self.position_y > SCREEN_HEIGHT - self.radius:
            print("you have gone past the edge of the screen")
            arcade.play_sound(self.sound_three)


    def snow_change(self):
        """changes snowman color to aquamarine"""
        self.color = arcade.csscolor.AQUAMARINE
    def change_again(self):
        """changes snowman color turquoise"""
        self.color = arcade.csscolor.TURQUOISE
    def reset_color(self):
        """resets the snowman's color back to white"""
        self.color = arcade.csscolor.WHITE

class CrescentSun:
    """Creation of a crescent sun"""
    def __init__(self, c_x, c_y, change_x, change_y, width, height, color, s_a, e_a):
        self.center_x = c_x
        self.center_y = c_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color
        self.start_angle = s_a
        self.end_angle = e_a

    def draw_crescent(self):
        arcade.draw_arc_filled(self.center_x,
                               self.center_y,
                               self.width,
                               self.height,
                               self.color,
                               self.start_angle,
                               self.end_angle)
    def update(self):
        """updating method for crescent sun"""
        self.center_y += self.change_y
        self.center_x += self.change_x

        if self.center_x < 0:
            self.center_x = self.width
            print("you have moved off the screen")
        if self.center_x > SCREEN_WIDTH:
            self.center_x = self.width
            print("you have moved off the screen")
        if self.center_y < 0:
            self.center_y = self.height
            print("you have moved off the screen")
        if self.center_y > SCREEN_HEIGHT:
            self.center_y = self.height
            print("you have moved off the screen")

    def rotate(self):
        """Rotation method for sun, click C"""
        self.start_angle += 45
        self.end_angle += 45

class Ground:
    def __init__(self):
        self.color = arcade.csscolor.GREEN

    def draw_ground(self):
        """Draws the Ground"""
        arcade.draw_rectangle_filled(0, 0, SCREEN_HEIGHT + 1000, SCREEN_WIDTH, self.color)

    def change_color(self):
        """Changes ground's color, based on left mouse click"""
        self.color = arcade.csscolor.LIGHT_GREEN

    def change_color_again(self):
        """Changes ground's color, based on right mouse click"""
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
        """creating two other sound variables"""

        self.sun = CrescentSun(SCREEN_WIDTH / 1.25, SCREEN_HEIGHT / 1.5, 0, 0, 50, 100, arcade.csscolor.GOLD, 90, 270)

        self.snowman = SnowMan(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4, 100, arcade.csscolor.WHITE)
        self.myGround = Ground()

        self.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()
        self.myGround.draw_ground()
        self.snowman.draw()
        self.sun.draw_crescent()

    def update(self, delta_time: float):
        self.snowman.update()
        self.sun.update()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.myGround.change_color()
            arcade.play_sound(self.sound_two)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            self.myGround.change_color_again()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.T:
            self.snowman.change_again()
            print("You set the snowman's color to turquoise")
        elif key == arcade.key.A:
            self.snowman.snow_change()
            print("You set the snowman's color to aquamarine")
        elif key == arcade.key.R:
            self.snowman.reset_color()
            print("You reset the snowman's color to white")
        elif key == arcade.key.UP:
            self.sun.change_y = MOVEMENT_SPEED
            print("you moved up")
        elif key == arcade.key.C:
            self.sun.rotate()
        elif key == arcade.key.DOWN:
            self.sun.change_y = -MOVEMENT_SPEED
            print("you moved down")
        elif key == arcade.key.RIGHT:
            self.sun.change_x = MOVEMENT_SPEED
            print("you moved right")
        elif key == arcade.key.LEFT:
            self.sun.change_x = -MOVEMENT_SPEED
            print("you moved left")
        else:
            print("command wasn't read correctly")

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.sun.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.sun.change_y = 0

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.snowman.position_y = y
        self.snowman.position_x = x


def main():
    window = MyGame()
    arcade.run()


main()