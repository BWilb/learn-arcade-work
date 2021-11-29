import arcade
import MainCharacter

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SPRITE_SCALING = 0.5
CAMERA_SPEED = 0.45
MOVEMENT_SPEED = int(input("User how fast would you like your character to move?: "))
GRAVITY = 0.30
COIN_COUNT = 100

class Coin(arcade.Sprite):
    def __int__(self, file_name, coin_scaling):
        super().__init__(file_name, coin_scaling)

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Final Project")
        self.character = MainCharacter.Main_Character
        self.character().__init__()
        self.game_scene = None
        self.physics_engine = None
        self.coin_list = None

        self.character_camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):
        self.game_scene = arcade.Scene()
        self.game_scene.add_sprite_list("Walls", use_spatial_hash=True)
        self.game_scene.add_sprite_list("Characters", use_spatial_hash=True)
        self.character.setup(self)

        map = "FinalProject.json"

        self.tile_map = arcade.load_tilemap(map, scaling=SPRITE_SCALING)
        self.wall_list = self.tile_map.sprite_lists["Walls"]

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.character,
            self.wall_list,
            gravity_constant=GRAVITY
        )

        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)
        else:
            arcade.set_background_color(arcade.color.GOLD)

    def on_draw(self):
        arcade.start_render()
        self.character_camera.use()
        self.wall_list.draw()
        self.character.draw()
        self.camera_gui.use()

        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.character_camera.position[0]:5.1f}, " \
               f"{self.character_camera.position[1]:5.1f})"

        arcade.draw_text(text, 10, 10, arcade.color.BLACK_LEATHER_JACKET, 20)

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT:
            self.character.change_x = MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.character.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.character.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.character.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.character.change_y = 0
        elif key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.character.change_x = 0

    def on_update(self, delta_time: float):
        self.character.update()

        self.physics_engine.update()
        self.scroll_to_player()

    def scroll_to_player(self):
        position = self.character.center_x - self.width / 2, \
                   self.character.center_y - self.height / 2
        self.character_camera.move_to(position, CAMERA_SPEED)

    def on_resize(self, width: float, height: float):
        self.character_camera.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))

def main():
    window = MyGame()
    window.setup()
    arcade.run()

main()