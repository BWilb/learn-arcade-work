import arcade
"""Triple quotations
are the best
"""
#faitharf
arcade.open_window(600, 600, "Drawing Example")

#arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0,400,300,0, arcade.csscolor.GREEN)

arcade.draw_rectangle_filled(100,300,20,60, arcade.csscolor.SADDLE_BROWN)

arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.GREEN)


arcade.draw_rectangle_filled(200,320,20,60,arcade.csscolor.SADDLE_BROWN)
arcade.draw_ellipse_filled(200,370,60,80,arcade.csscolor.GREEN)


"""arcade.draw_rectangle_filled(300,320,20,60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300,340,60,100, arcade.csscolor.DARK_RED, 0, 180)
"""


"""arcade.draw_rectangle_filled(400,320,20,60, arcade.csscolor.YELLOW)
arcade.draw_triangle_filled(400,400,370, 320,430,320, arcade.csscolor.AQUAMARINE)
"""

#2nd center, erd radius

arcade.finish_render()

arcade.run()