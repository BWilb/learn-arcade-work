import arcade
#this is how you import a library

"""
this is a sample of how you do a multi line comment
this program will cover: how to draw an object
"""
#this is how you do a single line comment

arcade.open_window(500, 600, "window")
#setting the background color
arcade.set_background_color(arcade.csscolor.BLACK)
#gretting erady to draw
arcade.start_render()

arcade.draw_circle_filled(0,0,50, arcade.csscolor.AQUA)

arcade.finish_render()

arcade.run()

print("y\n\"h")

