import arcade

arcade.open_window(500,500,"DRAWING EXAMPLE")

arcade.set_background_color(arcade.csscolor.DARK_BLUE)

arcade.start_render()

arcade.draw_rectangle_filled(250,150,500,300,(114, 160, 193))

arcade.draw_circle_filled(125, 125, 75, (240, 248, 255))
#this function draws the bottom of the snowman
arcade.draw_circle_filled(125, 225, 50, (240, 248, 255))
#this function draws the abdomen
arcade.draw_circle_filled(125,290,25,(240, 248, 255))
#this function draws the head
arcade.draw_circle_filled(115,295,6, (255, 3, 62))
#this function draws the left eye
arcade.draw_circle_filled(135,295,6,(255, 3, 62))
#this function draws the right eye


arcade.finish_render()
arcade.run()