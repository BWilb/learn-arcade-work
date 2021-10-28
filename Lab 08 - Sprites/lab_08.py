import random
import arcade

VADER_SCALING = 0.05
KENOBI_SCALING = 0.05
BLASTER_SCALING = 0.07
SABER_SCALING = 0.06
KENOBI_SPEED = int(input("How fast would you like Obi Wan Kenobi to move?: "))
BLASTER_COUNT = 50
SABER_COUNT = 50
SOUND_ONE = arcade.load_sound("laser4.wav")
SOUND_TWO = arcade.load_sound("laser13.wav")

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

class VaderSprite(arcade.Sprite):
    """separate class for my vader sprite"""
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1

class KenobiSprite(arcade.Sprite):
    """Separate class for my kenobi sprite"""
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0
        self.score = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.right > SCREEN_WIDTH:
            self.left = 0
        if self.left < 0:
            self.right = SCREEN_WIDTH
        if self.top > SCREEN_HEIGHT:
            self.bottom = 0
        if self.bottom < 0:
            self.top = SCREEN_HEIGHT

class Blaster(arcade.Sprite):
    """Separate class for my blasters"""

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

    def update(self):
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            # Reset the coin to a random spot above the screen
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)

class Saber(arcade.Sprite):
    """Separate class for my sabers"""
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

    def update(self):
        self.center_x += 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.left > SCREEN_WIDTH:
            # Reset the coin to a random spot above the screen
            self.center_y = random.randrange(SCREEN_HEIGHT)
            self.center_x = random.randrange(SCREEN_WIDTH)

class MyGame(arcade.Window):
    """Creation of my game class"""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Vader vs Kenobi")
        """Creation of my sprite objects"""
        self.sprite_list = None
        self.objects_list = None

        self.kenobi_sprite = None
        self.kenobi_score = None

        self.vader_sprite = None
        self.vader_score = None

        arcade.set_background_color(arcade.csscolor.SANDY_BROWN)

    def setup(self):

        self.sprite_list = arcade.SpriteList()
        self.objects_list = arcade.SpriteList()

        self.kenobi_score = 0
        self.kenobi_sprite = KenobiSprite("kenobi.png", KENOBI_SCALING)
        """Cite: Jesuschrist Jesus Obiwankenobi Obiwan Starwars Chruch. https://www.pngaaa.com/detail/1002504. 2020."""
        self.kenobi_sprite.center_x = 100
        self.kenobi_sprite.center_y = 300
        self.sprite_list.append(self.kenobi_sprite)

        self.vader_score = 0
        self.vader_sprite = VaderSprite("darth_vader.png", VADER_SCALING)
        """Cite: Download PNG image: Darth Vader PNG. https://pngimg.com/image/28352"""
        self.vader_sprite.center_x = 600
        self.vader_sprite.center_y = 500
        self.vader_sprite.change_x = random.randrange(-3, 20)
        self.vader_sprite.change_y = random.randrange(-3, 20)
        self.sprite_list.append(self.vader_sprite)

        for i in range(BLASTER_COUNT):
            blaster = Blaster("blaster.png", BLASTER_SCALING)
            """Cite: Star Wars Battlefront Wiki: Blaster Pistol. https://battlefront.fandom.com/wiki/Blaster_Pistol."""
            blaster.center_x = random.randrange(SCREEN_WIDTH)
            blaster.center_y = random.randrange(SCREEN_HEIGHT)
            self.objects_list.append(blaster)
        for j in range(SABER_COUNT):
            saber = Saber("dual_saber.png", SABER_SCALING)
            """Cite: Adaptive Saber Parts Lightsaber. https://www.pinterest.com/pin/235594624235964960/"""
            saber.center_x = random.randrange(SCREEN_WIDTH)
            saber.center_y = random.randrange(SCREEN_HEIGHT)
            self.objects_list.append(saber)

    def on_draw(self):
        arcade.start_render()
        if len(self.objects_list) != 0:
            self.objects_list.draw()
            self.sprite_list.draw()
        else:
            if self.kenobi_score > self.vader_score:
                arcade.draw_text("General Kenobi has won", 500, 400, arcade.csscolor.WHITE, 20)
                """Kenobi is the good sprite"""
                arcade.finish_render()
            elif self.vader_score > self.kenobi_score:
                arcade.draw_text("Darth Vader has won", 500, 400, arcade.csscolor.WHITE, 20)
                """Darth Vader is the bad sprite"""
                arcade.finish_render()

        arcade.draw_text(f"Kenobi's score: {self.kenobi_score}", 600, 200, arcade.csscolor.WHITE, 14)
        arcade.draw_text(f"Vader's score: {self.vader_score}", 600, 150, arcade.csscolor.WHITE, 14)
        """establishing score"""

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.DOWN:
            self.kenobi_sprite.change_y = -KENOBI_SPEED
        elif key == arcade.key.UP:
            self.kenobi_sprite.change_y = KENOBI_SPEED
        elif key == arcade.key.RIGHT:
            self.kenobi_sprite.change_x = KENOBI_SPEED
        elif key == arcade.key.LEFT:
            self.kenobi_sprite.change_x = -KENOBI_SPEED

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.DOWN:
            self.kenobi_sprite.change_y = 0
        elif key == arcade.key.UP:
            self.kenobi_sprite.change_y = 0
        elif key == arcade.key.RIGHT:
            self.kenobi_sprite.change_x = 0
        elif key == arcade.key.LEFT:
            self.kenobi_sprite.change_x = 0


    def update(self, delta_time):
        if self.kenobi_score > -10:
            self.kenobi_sprite.update()
            self.vader_sprite.update()
            self.objects_list.update()
            """checks to see if kenobi's score is above -10"""


        sprite_hit_list = arcade.check_for_collision(self.kenobi_sprite, self.vader_sprite)
        kenobi_hit_list = arcade.check_for_collision_with_list(self.kenobi_sprite, self.objects_list)
        vader_hit_list = arcade.check_for_collision_with_list(self.vader_sprite, self.objects_list)

        if sprite_hit_list:
            self.vader_score -= 3
            self.kenobi_score -= 2

        for object1 in kenobi_hit_list:
            object1.remove_from_sprite_lists()
            arcade.play_sound(SOUND_ONE)
            self.vader_score -= 1
            self.kenobi_score += 2

        for object2 in vader_hit_list:
            object2.remove_from_sprite_lists()
            arcade.play_sound(SOUND_TWO)
            self.kenobi_score -= 1
            self.vader_score += 2

def main():
    my_window = MyGame()
    my_window.setup()
    arcade.run()

main()
