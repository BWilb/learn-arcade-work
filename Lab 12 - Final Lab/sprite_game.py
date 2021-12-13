import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_SCALING = 0.25
MOVEMENT_SPEED = int(input("\nHow fast would you like to move?: "))

class German(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)
        self.change_x = 0
        self.health = 25

    def update(self):
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

class City:
    def __init__(self):
        self.background = None
        self.german_list = None
        self.ground_list = None

def city_one():
    city = City()
    city.ground_list = arcade.SpriteList()
    city.german_list = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        floor = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        floor.center_x = SCREEN_WIDTH
        floor.center_y = 16
        city.ground_list.append(floor)

    germans = random.randrange(1, 5)
    for german in range(germans):
        city.barbarian = German("german.png", SPRITE_SCALING)
        barbarian_successful = False

        while not barbarian_successful:

            city.barbarian.center_x = random.randrange(SCREEN_WIDTH)
            city.barbarian.center_y = 32

            german_hit_list = arcade.check_for_collision_with_list(city.barbarian, city.ground_list)

            german_german = arcade.check_for_collision_with_list(city.barbarian, city.german_list)

            if len(german_hit_list) == 0 and len(german_german) == 0:
                barbarian_successful = True

        city.german_list.append(city.barbarian)
    city.background = arcade.load_texture("naples.png")
    """Heath Elizabeth. Top Neighborhoods in Naples. Tripsavvy, 19 Oct 2020,
    https://www.tripsavvy.com/top-neighborhoods-in-naples-5079807. 
    Accessed Dec 12 2021."""
    return city

def city_two():
    city = City()
    city.ground_list = arcade.SpriteList()
    city.german_list = arcade.SpriteList()
    for x in range(0, SCREEN_WIDTH, 32):
        floor = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        floor.center_x = SCREEN_WIDTH
        floor.center_y = 16
        city.ground_list.append(floor)

    germans = random.randrange(1, 5)
    for german in range(germans):
        city.barbarian = German("german.png", SPRITE_SCALING)
        barbarian_successful = False

        while not barbarian_successful:

            city.barbarian.center_x = random.randrange(SCREEN_WIDTH)
            city.barbarian.center_y = 32

            german_hit_list = arcade.check_for_collision_with_list(city.barbarian, city.ground_list)

            german_german = arcade.check_for_collision_with_list(city.barbarian, city.german_list)

            if len(german_hit_list) == 0 and len(german_german) == 0:
                barbarian_successful = True

        city.german_list.append(city.barbarian)

    city.background = arcade.load_texture("rome.png")
    """Rome. Travel Pulse, 05 Nov 2021, 
    https://www.travelpulse.com/destinations/europe/italy/rome.html. Accessed Dec 12 2021. """

    return city

def city_three():
    city = City()
    city.ground_list = arcade.SpriteList()
    city.german_list = arcade.SpriteList()

    for x in range(0, SCREEN_WIDTH, 32):
        floor = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        floor.center_x = SCREEN_WIDTH
        floor.center_y = 16
        city.ground_list.append(floor)

    germans = random.randrange(1, 5)
    for german in range(germans):
        city.barbarian = German("german.png", SPRITE_SCALING)
        barbarian_successful = False

        while not barbarian_successful:

            city.barbarian.center_x = random.randrange(SCREEN_WIDTH)
            city.barbarian.center_y = 32

            german_hit_list = arcade.check_for_collision_with_list(city.barbarian, city.ground_list)

            german_german = arcade.check_for_collision_with_list(city.barbarian, city.german_list)

            if len(german_hit_list) == 0 and len(german_german) == 0:
                barbarian_successful = True

        city.german_list.append(city.barbarian)
    city.background = arcade.load_texture("genoa.png")
    """Gabriele, Amanda. How to eat your way through Genoa, Italy - and see
    some sights along the way. Travel and Leisure, 19 Jan 2020, 
    https://www.travelandleisure.com/food-drink/what-to-do-and-eat-in-genoa-italy.
    Accessed Dec 12 2021.
    """

    return city

def city_four():
    city = City()
    city.ground_list = arcade.SpriteList()
    city.german_list = arcade.SpriteList()
    for x in range(0, SCREEN_WIDTH, 32):

        floor = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        floor.center_x = SCREEN_WIDTH
        floor.center_y = 16
        city.ground_list.append(floor)

    germans = random.randrange(1, 5)
    for german in range(germans):
        city.barbarian = German("german.png", SPRITE_SCALING)
        barbarian_successful = False

        while not barbarian_successful:

            city.barbarian.center_x = random.randrange(SCREEN_WIDTH)
            city.barbarian.center_y = 32

            german_hit_list = arcade.check_for_collision_with_list(city.barbarian, city.ground_list)

            german_german = arcade.check_for_collision_with_list(city.barbarian, city.german_list)

            if len(german_hit_list) == 0 and len(german_german) == 0:
                barbarian_successful = True

        city.german_list.append(city.barbarian)
    city.background = arcade.load_texture("venice.png")
    """Karsten, Matthew. 30 best things to do in Venice (Italy's floating city).
    Expert Vagabond, 24 Nov 2021, https://expertvagabond.com/venice-italy-things-to-do/.
    Accessed Dec 10 2021.
    """
    return city

class RomanGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Rome's final stand")
        self.player_list = arcade.SpriteList()
        self.cities = []
        self.caesar_sprite = None
        self.caesar_health = 200
        self.caesar_score = None
        self.physics_engine = None
        self.caesar_score = None
        self.city = City()
        self.german_count_one = None
        self.german_count_two = None
        self.german_count_three = None
        self.german_count_four = None
        self.german_total = 0
        self.german_amount = 0

    def setup(self):

        self.player_list = arcade.SpriteList()

        self.caesar_sprite = arcade.Sprite("caesar.png", SPRITE_SCALING)
        self.caesar_sprite.center_x = 40
        self.caesar_sprite.center_y = 40
        self.caesar_score = 0
        self.player_list.append(self.caesar_sprite)

        self.city = city_one()
        self.german_count_one = city_one().german_list
        self.cities.append(self.city)

        self.city = city_two()
        self.german_count_two = city_two().german_list
        self.cities.append(self.city)

        self.city = city_three()
        self.german_count_three = city_three().german_list
        self.cities.append(self.city)

        self.city = city_four()
        self.german_count_four = city_four().german_list
        self.cities.append(self.city)

        self.current_city = 0
        self.physics_engine = arcade.PhysicsEngineSimple(self.caesar_sprite,
                                                         self.cities[self.current_city].ground_list)
        for i in range(len(self.cities)):
            self.german_amount += len(self.cities[i].german_list)

    def on_draw(self):
        arcade.start_render()
        if self.german_amount > 0 and self.caesar_health >= 0:
            arcade.draw_lrwh_rectangle_textured(0, 0,
                                                SCREEN_WIDTH, SCREEN_HEIGHT, self.cities[self.current_city].background)
            self.cities[self.current_city].ground_list.draw()

            if self.current_city == 0:
                self.cities[self.current_city].german_list.draw()

            elif self.current_city == 1:
                self.cities[self.current_city].german_list.draw()

            elif self.current_city == 2:
                self.cities[self.current_city].german_list.draw()
            elif self.current_city == 3:
                self.cities[self.current_city].german_list.draw()
            self.player_list.draw()

        elif self.german_amount == 0:
            arcade.draw_text("Congrats, you defeated every german", 400, 400, arcade.csscolor.WHITE)
            arcade.finish_render()

        elif self.caesar_health <= 0:
            arcade.draw_text("Unfortunately you have died.", 400, 400, arcade.csscolor.WHITE)
            arcade.finish_render()

        arcade.draw_text(f"Score: {self.caesar_score}", 400, 50, arcade.csscolor.GOLD)
        arcade.draw_text(f"Current health: {self.caesar_health}", 400, 25, arcade.csscolor.GOLD)
        arcade.draw_text(f"Remaining Germans: {self.german_amount}", 400, 10, arcade.csscolor.GOLD)

    def on_update(self, delta_time: float):
        if self.german_amount > 0 and self.caesar_health >= 0:
            self.player_list.update()
            self.caesar_sprite.update()
            self.physics_engine.update()
            self.city.german_list.update()
            self.cities[self.current_city].german_list.update()

        caesar_hit_list = arcade.check_for_collision_with_list(self.caesar_sprite,
                                                               self.cities[self.current_city].german_list)

        for caesar in caesar_hit_list:
            german_ones = self.german_count_one
            german_twos = self.german_count_two
            german_threes = self.german_count_three
            german_fours = self.german_count_four
            attack = random.randrange(0, 60)
            german_attack = random.randrange(0, 36)

            if self.current_city == 0:
                for i in range(len(german_ones)):
                    german_ones[i].health -= attack
                    if german_ones[i].health <= 0:
                        caesar.remove_from_sprite_lists()
                        self.caesar_score += 1

            elif self.current_city == 1:
                for i in range(len(german_twos)):
                    german_twos[i].health -= attack
                    if german_twos[i].health <= 0:
                        caesar.remove_from_sprite_lists()
                        self.caesar_score += 1

            elif self.current_city == 2:
                for i in range(len(german_threes)):
                    german_threes[i].health -= attack
                    if german_threes[i].health <= 0:
                        caesar.remove_from_sprite_lists()
                        self.caesar_score += 1

            elif self.current_city == 3:
                for i in range(len(german_fours)):
                    german_fours[i].health -= attack
                    if german_fours[i].health < 0:
                        caesar.remove_from_sprite_lists()
                        self.caesar_score += 1

            self.german_amount -= 1
            self.caesar_health -= german_attack

        if self.caesar_sprite.center_x > SCREEN_WIDTH and self.current_city == 0:
            self.current_city = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.caesar_sprite,
                                                             self.cities[self.current_city].ground_list)
            self.caesar_sprite.center_x = 0

        elif self.caesar_sprite.center_x <= 0 and self.current_city == 1:
            self.current_city = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.caesar_sprite,
                                                             self.cities[self.current_city].ground_list)
            self.caesar_sprite.center_x = SCREEN_WIDTH

        elif self.caesar_sprite.center_x > SCREEN_WIDTH and self.current_city == 1:
            self.current_city = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.caesar_sprite,
                                                             self.cities[self.current_city].ground_list)
            self.caesar_sprite.center_x = 0

        elif self.caesar_sprite.center_x < 0 and self.current_city == 2:
            self.current_city = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.caesar_sprite,
                                                             self.cities[self.current_city].ground_list)
            self.caesar_sprite.center_x = SCREEN_WIDTH

        elif self.caesar_sprite.center_x > SCREEN_WIDTH and self.current_city == 2:
            self.current_city = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.caesar_sprite,
                                                             self.cities[self.current_city].ground_list)
            self.caesar_sprite.center_x = 0

        elif self.caesar_sprite.center_x < 0 and self.current_city == 3:
            self.current_city = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.caesar_sprite,
                                                             self.cities[self.current_city].ground_list)
            self.caesar_sprite.center_x = SCREEN_WIDTH

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT:
            self.caesar_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.caesar_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.caesar_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.caesar_sprite.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.caesar_sprite.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.caesar_sprite.change_y = 0

def main():
    """ Main method """
    window = RomanGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()