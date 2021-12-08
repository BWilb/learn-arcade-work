import arcade
import main
import german
import roman_soldier

class City:
    def __init__(self):
        self.background = None
        self.enemy_list = []


class CaesarSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.caesar_health = 200
        self.troop_list = [50]
        self.center_x
        self.center_y
