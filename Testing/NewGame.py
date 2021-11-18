import arcade
import random
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
BOX_COUNT = 50
SCALING = 0.5
MOVEMENT_SPEED = int(input("How fast would you like your character to go"))
TITLE = "History Game"

class Room:
    def __init__(self):
        self.background = None

class HistoryGame(arcade.Window):
    def __init__(self):
        super.__init__(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
        self.scene = None

        self.character = None

    def setup(self):
        self.scene = arcade.Scene()

        self.scene.add_sprite_list("Characters")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)

        self.character = arcade.Sprite("character.png", SCALING)
        self.character.center_x = random.randrange(SCREEN_WIDTH)
        self.character.center_y = random.randrange(SCREEN_HEIGHT)
        self.scene.add_sprite("Characters", self.character)

        for x in range(0, SCREEN_HEIGHT, 32):
            wall = arcade.Sprite("boxCrate_double.png", SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)
        for y in range(SCREEN_HEIGHT / 2, SCREEN_HEIGHT, 32):
            wall = arcade.Sprite("boxCrate_double.png", SCALING)
            wall.center_x = 500
            wall.center_y = y
            self.scene.add_sprite("Walls", wall)

    def on_update(self, delta_time: float):
        self.

    def on_draw(self):
        arcade.start_render()

        self.scene.draw()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.UP:
            arcade.
