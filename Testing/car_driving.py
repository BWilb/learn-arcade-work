import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
class CarBody:
    def __init__(self, position_x, position_y, width, height, change_x, change_y, color):

        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, self.color)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < self.width:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.width:
            self.change_x *= -1

        if self.position_y < self.height:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.height:
            self.change_y *= -1

class CarWheels:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        self.position_y += self.change_y

        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1

class MyCar(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

        self.my_car = CarBody(50, 50, 50, 50, 2, 0, arcade.color.CORN)
        self.tire = CarWheels(35, 25, 2, 0, arcade.color.BLACK)
        self.tire = CarWheels()

