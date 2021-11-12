import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Avatar(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = None
        self.center_y = None

class Room:
    def __init__(self):
        self.background = None
        self.wall_list = None
        self.object_list = None
class MyGame(arcade.Window):
    def __init__(self):
        super.__init__():
