import arcade

def draw_squares():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)

def first_square():
    for row in range(0, 300, 10):
        for column in range(0, 300, 10):
            x = column
            y = row
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.csscolor.WHITE)
def second_square():
    for row in range(0, 300, 10):
        for column in range(300, 600, 10):
            x = column
            y = row
            if x % 20 != 0:
                arcade.draw_rectangle_filled(x + 5, y + 5, 5, 5, arcade.csscolor.BLACK)
            else:
                arcade.draw_rectangle_filled(x + 5, y + 5, 5, 5, arcade.csscolor.WHITE)
def third_square():
    for row in range(5, 300, 10):
        for column in range(605, 900, 10):
            x = column
            y = row
            if y % 4 == 3:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.csscolor.BLACK)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.csscolor.WHITE)
def fourth_square():
    for row in range(0, 300, 10):
        for column in range(900, 1200, 10):
            x = column
            y = row
            if y % 20 == 0 and x % 20 == 0:
                arcade.draw_rectangle_filled(x + 5, y + 5, 5, 5, arcade.csscolor.WHITE)
            else:
                arcade.draw_rectangle_filled(x + 5, y + 5, 5, 5, arcade.csscolor.BLACK)
def fifth_square():
    for row in range(30):
        for column in range(30 - row):
            x = column * 10
            y = row * 10
            arcade.draw_rectangle_filled(305 - x, 305 + y, 5, 5, arcade.csscolor.WHITE)
def sixth_square():
    for row in range(30):
        for column in range(30 - row):
            x = column * 10
            y = row * 10
            arcade.draw_rectangle_filled(x + 305, y + 305, 5, 5, arcade.csscolor.WHITE)
def seventh_square():
    for row in range(30):
        for column in range(row):
            x = column * 10
            y = row * 10
            arcade.draw_rectangle_filled(x + 605, y + 305, 5, 5, arcade.csscolor.WHITE)
def eighth_square():
    for row in range(30):
        for column in range(30 - row):
            print("")
        for column in range(row + 1):
            x = column * 10
            y = row * 10
            arcade.draw_rectangle_filled(1200 - x, 305 + y, 5, 5, arcade.csscolor.WHITE)
def main():
    arcade.open_window(1200, 600, "Lab 05")
    arcade.set_background_color((245, 245, 220))

    arcade.start_render()

    draw_squares()
    first_square()
    second_square()
    third_square()
    fourth_square()
    fifth_square()
    sixth_square()
    seventh_square()
    eighth_square()

    arcade.finish_render()

    arcade.run()

main()