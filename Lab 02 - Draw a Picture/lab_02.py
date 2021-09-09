import arcade
"""For lab 2
I have drawn a snow man in the middle of winter, with a couple of trees in the background,
along with the sun. I know that the drawing of the leaves remaining on the trees isn't realistic. 
Each function's comment is below the exact function: just for clarification
"""
arcade.open_window(500, 500, "DRAWING EXAMPLE")

arcade.set_background_color(arcade.csscolor.DARK_BLUE)

arcade.start_render()

arcade.draw_rectangle_filled(250, 150, 500, 300, (114, 160, 193))

"""These set of functions draw a snowman"""
arcade.draw_circle_filled(125, 125, 75, (240, 248, 255))
# this function draws the bottom of the snowman
arcade.draw_point(125, 125, (0, 0, 0), 10)
# this function draws the button for the bottom of the snowman
arcade.draw_line(173, 225, 200, 180, (150, 113, 23), 10)
# this function and the next function after this one draw the arms of the snow man
arcade.draw_line(77, 225, 50, 180, (150, 113, 23), 10)
arcade.draw_circle_filled(125, 225, 50, (240, 248, 255))
# this function draws the abdomen
arcade.draw_point(125, 225, (0, 0, 0), 10)
# this function draws the button on the abdomen
arcade.draw_circle_filled(125, 290, 25, (240, 248, 255))
# this function draws the head
arcade.draw_line(100, 315, 150, 315, (61, 43, 31), 5)
# this function draws the bottom of the hat
arcade.draw_lrtb_rectangle_filled(112.5, 137.5, 335, 315, (61, 43, 31))
# this function drwas the top of the hat
arcade.draw_circle_filled(115, 295, 6, (255, 3, 62))
# this function draws the left eye
arcade.draw_circle_filled(135, 295, 6, (255, 3, 62))
# this function draws the right eye
arcade.draw_arc_filled(125,
                        278,
                        20,
                        15,
                        (59, 68, 75),
                        180,
                        360
                        )
# This function draws the smile
arcade.draw_point(125, 285, (59, 68, 75), 5)
# This function draws the nose

"""These next set of functions draw a tree"""
arcade.draw_rectangle_filled(400, 340, 25, 125, arcade.csscolor.SADDLE_BROWN)
# this function draws a pine tree
arcade.draw_line(410, 340, 440, 370, arcade.csscolor.SADDLE_BROWN, 10)
# this function draws the right branch of the tree, the next function will draw the left branch
arcade.draw_line(390, 340, 360, 370, arcade.csscolor.SADDLE_BROWN, 10)
arcade.draw_triangle_filled(
    360,
    402.5,
    440,
    402.5,
    400,
    450,
    (59, 122, 87))
# This function draws the leaves on the tree

"""This next set of functions draw a sun"""
arcade.draw_circle_filled(60, 450, 25, (255, 191, 0))
# This function draws the sun
arcade.draw_line(60, 425, 60, 405, (255, 191, 0), 6)
# this function and the next three functions draw rays eminating from the sun
arcade.draw_line(85, 450, 105, 450, (255, 191, 0), 6)
arcade.draw_line(60, 475, 60, 495, (255, 191, 0), 6)
arcade.draw_line(35, 450, 15, 450, (255, 191, 0), 6)

"""This next set of functions draw a warning ice sign"""
arcade.draw_lrtb_rectangle_filled(330, 360, 120, 35, (162, 162, 208))
arcade.draw_lrtb_rectangle_filled(270, 420, 200, 120, (61, 12, 2))
arcade.draw_text("Caution Slippery!", 280, 160, (227, 38, 54))

arcade.draw_text("Frosty The Snowman", 175, 450, (240, 220, 130))
# This function draws the text--> Frost the Snowman
arcade.finish_render()
arcade.run()