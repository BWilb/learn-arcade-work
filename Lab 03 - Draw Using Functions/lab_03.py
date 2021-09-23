import arcade
"""
In this lab I intend to draw the basic outline of a city
"""
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
def draw_concrete():
    """This function highlights the concrete of the small city"""
    arcade.draw_lrtb_rectangle_filled(0, 600, 200, 0, (110, 127, 128))

def draw_building(x, y, w, h):
    """This function draws each building of the city, the parameters take in values for adjusting center, height, and
    width
    each building is designed so that they overlap with each other
    """
    arcade.draw_rectangle_filled(0 + x, 0 + y, 50 + w, 50 + h, (132, 132, 130))

def draw_window(x, y, w, h):
    """this function draws about six windows for the two taller buildings.
    the window function takes in similar parameters as the draw building function
    but performs specific operations according to the dynamics of both buildings
    """
    arcade.draw_rectangle_filled(x - 25, y, w / 2, h/4, (255, 191, 0))
    arcade.draw_rectangle_filled(x + 25, y, w / 2, h/4, (255, 191, 0))
    arcade.draw_rectangle_filled(x - 25, y - 50, w / 2, h / 4, (255, 191, 0))
    arcade.draw_rectangle_filled(x + 25, y - 50, w / 2, h/4, (255, 191, 0))
    arcade.draw_rectangle_filled(x + 25, y + 50, w / 2, h / 4, (255, 191, 0))
    arcade.draw_rectangle_filled(x - 25, y + 50, w / 2, h / 4, (255, 191, 0))

def draw_door(x, y, w, h):
    """this function draws a door for the third building.
    just like with the window function, the operations and size of the door
    pertain to the department stores characteristics
    """
    arcade.draw_rectangle_filled(x, y - 25, w / 4, h, (193, 154, 107))

def draw_right_hill():
    """this function draws the hill on the right side of the screen"""
    arcade.draw_arc_filled(500, 200, 250, 300, (0, 106, 78), 0, 180)

def draw_left_hill():
    """his function draws the hill on the left side of the screen"""
    arcade.draw_arc_filled(50, 200, 250, 300, (0, 106, 78), 0, 180)

def draw_spire(x, y, w, h):
    """this function draws a spire for the two taller buildings"""
    arcade.draw_line(x, y, w, h, (112, 54, 66), 10)

def draw_squat_windows():
    """this function draws windows for the department store
    according to the specifications of the building
    """
    arcade.draw_rectangle_filled(387.5, 256.3, 25, 25, (127, 255, 212))
    arcade.draw_rectangle_filled(262.5, 256.3, 25, 25, (127, 255, 212))

def draw_clouds():
    """this function draws each cloud 100 units above the hill on the right
    and 75 units from each clouds center
    """
    arcade.draw_arc_filled(500, 400, 150, 100, (242, 243, 244), 0, 180)
    arcade.draw_arc_filled(425, 400, 150, 100, (242, 243, 244), 0, 180)

def draw_sun():
    """This function draws a sun, plus rays emanating from it"""
    arcade.draw_circle_filled(250, 400, 25, (255, 126, 0))
    arcade.draw_line(250, 375, 250, 345, (255, 126, 0))
    arcade.draw_line(250, 425, 250, 455, (255, 126, 0))
    arcade.draw_line(225, 400, 195, 400, (255, 126, 0))
    arcade.draw_line(275, 400, 305, 400, (255, 126, 0))

    arcade.draw_line(227, 412.5, 195, 432.5, (255, 126, 0))
    arcade.draw_line(227, 387.5, 195, 357.5, (255, 126, 0))
    arcade.draw_line(273, 412.5, 305, 432.5, (255, 126, 0))
    arcade.draw_line(273, 387.5, 305, 357.5, (255, 126, 0))

def draw_street():
    """this function draws the road of the city"""
    arcade.draw_lrtb_rectangle_filled(0, 600, 150, 100, (61, 43, 31))
    arcade.draw_lrtb_rectangle_filled(0, 50, 130, 120, (255, 225, 53))
    arcade.draw_lrtb_rectangle_filled(100, 150, 130, 120, (255, 225, 53))
    arcade.draw_lrtb_rectangle_filled(200, 250, 130, 120, (255, 225, 53))
    arcade.draw_lrtb_rectangle_filled(300, 350, 130, 120, (255, 225, 53))
    arcade.draw_lrtb_rectangle_filled(400, 450, 130, 120, (255, 225, 53))
    arcade.draw_lrtb_rectangle_filled(500, 550, 130, 120, (255, 225, 53))

def draw_advertisement():
    """This function draws a ground sign advertising the department store
    sign styled in order to fit the text
    """
    arcade.draw_lrtb_rectangle_filled(110, 320, 80, 10, (0, 0, 0))
    arcade.draw_text("department store, next left", 120, 35, (255, 255, 0))

def main():
    """This function is the main function, I will be calling all my other functions within this function"""
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "lab 3")

    arcade.set_background_color(arcade.csscolor.SKY_BLUE)

    arcade.start_render()

    draw_concrete()

    draw_advertisement()

    draw_sun()

    draw_clouds()

    draw_right_hill()
    draw_left_hill()

    draw_street()

    draw_building(100, 300, 45, 150)
    draw_window(100, 300, 45, 150)
    draw_spire(97.5, 400, 97.5, 450)

    draw_building(175, 275, 50, 100)
    draw_window(175, 275, 50, 100)
    draw_spire(175, 350, 175, 400)

    draw_building(325, 225, 200, 75)
    draw_door(325, 225, 200, 75)
    draw_squat_windows()

    arcade.finish_render()

    arcade.run()

main()