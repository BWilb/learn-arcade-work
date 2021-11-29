import arcade
SPRITE_SCALING = 0.5

class Main_Character(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.character = None
        self.character_score = None
        self.character_hit = None

    def description(self):
        print("This is the main character. Her name is Billy. Billy wants to go on an adventure")

    def setup(self):
        self.character = arcade.Sprite("character.png", SPRITE_SCALING)
        self.character.center_x = 50
        self.character.center_y = 50
        self.character_score = 0
        self.character_hit = 0