import arcade

MOVEMENT_SPEED = 10
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 900

class Car(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

    def draw_car(self, center_x, center_y, c_x, c_y, radius, width, height, color):
        arcade.draw_rectangle_filled(center_x, center_y, width, height, color)
        arcade.draw_circle_filled(center_x - 25, center_y - (radius / 2), radius, color)
        arcade.draw_circle_filled(center_x + 25, center_y - (radius / 2), radius, color)

class New_Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "New Game")

        self.sprite_list = None
        self.object_list = None

    def set_up(self):
        self.sprite_list = arcade.SpriteList()