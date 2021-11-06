import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_SCALING = 0.25
STONE_SCALING = 0.25
GRASS_SCALING = 0.25
OBJECT_SCALE = 0.25
SILVER_COINS = 50
DIAMOND_COUNT = 25
SOUND_ONE = arcade.load_sound("laser4.wav")

MOVEMENT_SPEED = int(input("how fast would you like your character to move?: "))


class Room:
    def __init__(self):
        self.wall_list = None
        self.coin_list = None
        self.background = None


def create_roomone():
    room = Room()
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    wall_coordinates = [[200, 400],
                        [232, 400],
                        [264, 400],
                        [296, 400],
                        [328, 400],
                        [350, 400]]

    second_coordinates = [[416, 400],
                          [448, 400],
                          [480, 400]]

    third_coordinates = [[432, 120],
                         [464, 120],
                         [496, 120],
                         [528, 120]]

    wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
    wall.center_x = 320
    wall.center_y = 120
    room.wall_list.append(wall)

    wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
    wall.center_x = 352
    wall.center_y = 120
    room.wall_list.append(wall)

    wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
    wall.center_x = 384
    wall.center_y = 120
    room.wall_list.append(wall)

    for x in range(0, SCREEN_WIDTH, 32):
        """Controls top wall"""
        wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
        wall.center_x = x
        wall.center_y = SCREEN_HEIGHT - 16
        room.wall_list.append(wall)

    for y2 in range(600, 256, -32):
        """Controls top part of right wall"""
        wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
        wall.center_x = SCREEN_WIDTH - 16
        wall.center_y = y2 - 16
        room.wall_list.append(wall)

    for x2 in range(45, SCREEN_WIDTH, 32):
        """Controls bottom wall"""
        wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
        wall.center_x = x2
        wall.center_y = 8
        room.wall_list.append(wall)

    for xy in range(SCREEN_HEIGHT, 0, -32):
        """Controls left wall"""
        wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
        wall.center_x = 16
        wall.center_y = xy - 16
        room.wall_list.append(wall)

    for wall_coordinate in wall_coordinates:
        """Controls a section of blocks in middle"""
        wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
        wall.center_x = wall_coordinate[0]
        wall.center_y = wall_coordinate[1]
        room.wall_list.append(wall)

    for second_coordinate in second_coordinates:
        """Controls a section of blocks in middle """
        wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
        wall.center_x = second_coordinate[0]
        wall.center_y = second_coordinate[1]
        room.wall_list.append(wall)

    for third_coordinate in third_coordinates:
        """Controls a section of blocks in middle"""
        wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
        wall.center_x = third_coordinate[0]
        wall.center_y = third_coordinate[1]
        room.wall_list.append(wall)

    for i in range(SILVER_COINS):
        """Places coins in random spots"""
        coin = arcade.Sprite("silver_coin.png", OBJECT_SCALE)
        coin_placed = False

        while not coin_placed:

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            wall_hit_list = arcade.check_for_collision_with_list(coin, room.wall_list)

            coin_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list)

            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                coin_placed = True

        room.coin_list.append(coin)

        room.background = arcade.load_texture("black.jpeg")
        """4 Paint Texture Black and White Texture (JPG).
        Mail Chimp. https://www.onlygfx.com/4-paint-texture-black-and-white-texture-jpg/. 2021"""

    return room


def create_roomtwo():
    room = Room()
    """FREE 30+ High Quality Blue Textures for Graphic Designers in PSD | Vector EPS.
    FreeCreatives. https://www.freecreatives.com/textures/blue-texture.html. 2021"""
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()

    for x in range(0, 384, 32):
        """left side of ground"""
        wall = arcade.Sprite("grassMid.png", GRASS_SCALING)
        wall.center_x = x
        wall.center_y = 16
        room.wall_list.append(wall)

    for x2 in range(416, SCREEN_WIDTH + 16, 32):
        "right side of ground"
        wall = arcade.Sprite("grassMid.png", GRASS_SCALING)
        wall.center_x = x2
        wall.center_y = 16
        room.wall_list.append(wall)

    for y in range(SCREEN_HEIGHT, 256, -32):
        """opening of cave"""
        wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
        wall.center_x = 16
        wall.center_y = y
        room.wall_list.append(wall)

    for i in range(DIAMOND_COUNT):
        """Places diamonds in random spots"""

        room.diamond = arcade.Sprite("gemYellow.png", OBJECT_SCALE)
        coin_placed_successfully = False

        while not coin_placed_successfully:

            room.diamond.center_x = random.randrange(SCREEN_WIDTH)
            room.diamond.center_y = random.randrange(SCREEN_HEIGHT)

            wall_hit_list = arcade.check_for_collision_with_list(room.diamond, room.wall_list)

            coin_hit_list = arcade.check_for_collision_with_list(room.diamond, room.coin_list)

            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                coin_placed_successfully = True

        room.coin_list.append(room.diamond)

    room.background = arcade.load_texture("blue.jpeg")

    return room


def create_roomthree():
    room = Room()
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()

    for y1 in range(SCREEN_HEIGHT, -32, -32):
        """controls left side of room 3"""
        wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
        wall.center_x = 0
        wall.center_y = y1
        room.wall_list.append(wall)

    for y2 in range(SCREEN_HEIGHT, -32, -32):
        """controls the right side of room 3"""
        wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
        wall.center_x = SCREEN_WIDTH - 16
        wall.center_y = y2
        room.wall_list.append(wall)

    for x1 in range(0, SCREEN_WIDTH + 16, 32):
        """Controls the bottom of room 3"""
        wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
        wall.center_x = x1
        wall.center_y = 0
        room.wall_list.append(wall)

    for x2 in range(0, 384, 32):
        """Controls top left of room 3"""
        wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
        wall.center_x = x2
        wall.center_y = SCREEN_HEIGHT
        room.wall_list.append(wall)

    for x3 in range(416, SCREEN_WIDTH, 32):
        """controls top right of room 3"""
        wall = arcade.Sprite("stoneRight.png", STONE_SCALING)
        wall.center_x = x3
        wall.center_y = SCREEN_HEIGHT
        room.wall_list.append(wall)

    room.background = arcade.load_texture("black.jpeg")
    return room


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 9")
        self.rooms = []
        self.current_room = 0
        self.character_hit = 0
        """establishment of tracker variable"""
        self.player_list = None
        self.character = None
        self.physics_engine = None
        self.room = Room()

    def setup(self):
        """setup of game"""
        self.player_list = arcade.SpriteList()

        self.character = arcade.Sprite("character.png", SPRITE_SCALING)
        self.character.center_x = 40
        self.character.center_y = 40
        self.character_score = 0
        self.player_list.append(self.character)

        self.room = create_roomone()
        self.rooms.append(self.room)

        self.room = create_roomtwo()
        self.rooms.append(self.room)

        self.room = create_roomthree()
        self.rooms.append(self.room)

        self.current_room = 0
        self.physics_engine = arcade.PhysicsEngineSimple(self.character,
                                                         self.rooms[self.current_room].wall_list)

    def on_draw(self):
        """Drawing of everything in main game"""
        arcade.start_render()

        if self.character_hit != DIAMOND_COUNT + SILVER_COINS:
            arcade.draw_lrwh_rectangle_textured(0, 0,
                                                SCREEN_WIDTH, SCREEN_HEIGHT, self.rooms[self.current_room].background)
            self.rooms[self.current_room].wall_list.draw()
            if self.current_room == 0:
                self.rooms[self.current_room].coin_list.draw()
            elif self.current_room == 1:
                self.rooms[self.current_room].coin_list.draw()
            elif self.current_room == 2:
                self.rooms[self.current_room].coin_list.draw()
            self.character.draw()
        elif self.character_hit == (DIAMOND_COUNT + SILVER_COINS):
            arcade.draw_text("Game Over: No more objects left!", 400, 400, arcade.csscolor.WHITE)
            arcade.finish_render()

        arcade.draw_text(f"Score: {self.character_score}", 400, 50, arcade.csscolor.GOLD)

    def on_update(self, delta_time: float):
        if self.character_hit < SILVER_COINS + DIAMOND_COUNT:
            self.character.update()
            self.physics_engine.update()
            self.room.coin_list.update()
        character_hit_list = arcade.check_for_collision_with_list(self.character,
                                                                  self.rooms[self.current_room].coin_list)
        for coin_object in character_hit_list:
            coin_object.remove_from_sprite_lists()
            self.character_score += 1
            arcade.play_sound(SOUND_ONE)
            self.character_hit += 1

        if self.character.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.character,
                                                             self.rooms[self.current_room].wall_list)
            self.character.center_x = 0

        elif self.character.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.character,
                                                             self.rooms[self.current_room].wall_list)
            self.character.center_x = SCREEN_WIDTH

        elif self.character.center_y < 0 and self.current_room == 1:
            self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.character,
                                                             self.rooms[self.current_room].wall_list)
            self.character.center_x = 400
            self.character.center_y = SCREEN_HEIGHT

        elif self.character.center_y > SCREEN_HEIGHT and self.current_room == 2:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.character,
                                                             self.rooms[self.current_room].wall_list)
            self.character.center_x = 400
            self.character.center_y = 0

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.UP:
            self.character.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.character.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.character.change_x = MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.character.change_x = -MOVEMENT_SPEED

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.character.change_y = 0
        elif key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.character.change_x = 0


def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()