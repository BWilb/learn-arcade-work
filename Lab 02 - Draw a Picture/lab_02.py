import arcade
"""For lab 2
I have drawn a snow man in the middle of winter, with a couple of trees in the background,
along with the sun. I know that the drawing of the leaves remaining on the trees isn't realistic. 
"""
arcade.open_window(500,500,"DRAWING EXAMPLE")

arcade.set_background_color(arcade.csscolor.DARK_BLUE)

arcade.start_render()

arcade.draw_rectangle_filled(250, 150, 500, 300, (114, 160, 193))

arcade.draw_circle_filled(125, 125, 75, (240, 248, 255))
# this function draws the bottom of the snowman
arcade.draw_circle_filled(125, 225, 50, (240, 248, 255))
# this function draws the abdomen
arcade.draw_circle_filled(125, 290, 25, (240, 248, 255))
# this function draws the head
arcade.draw_circle_filled(115, 295, 6, (255, 3, 62))
# this function draws the left eye
arcade.draw_circle_filled(135, 295, 6, (255, 3, 62))
# this function draws the right eye
arcade.draw_arc_filled(125,
                        278,
                        20,
                        15,
                        (251, 206, 177),
                        180,
                        360
                        )
arcade.draw_rectangle_filled(400, 340, 25, 125, arcade.csscolor.SADDLE_BROWN)
# this function draws a pine tree
arcade.draw_triangle_filled(
    360,
    402.5,
    440,
    402.5,
    400,
    450,
    (59, 122, 87))
# This functin draws the leaves on the tree
arcade.finish_render()
arcade.run()