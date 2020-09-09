import arcade

arcade.open_window(800, 600, "Lab 2")

arcade.set_background_color(arcade.color.AZURE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 180, 0, arcade.color.BUD_GREEN)

# Draw a house.
arcade.draw_lrtb_rectangle_filled(70, 400, 400, 150, arcade.color.CARROT_ORANGE)
arcade.draw_triangle_filled(65, 400, 225, 500, 405, 400, arcade.color.BLACK)
arcade.draw_rectangle_filled(225, 225, 100, 150, arcade.color.BLUE_SAPPHIRE)
arcade.draw_circle_filled(255, 240, 7, arcade.color.BROWN)

# Draw a tree.
arcade.draw_rectangle_filled(700, 200, 60, 100, arcade.color.DARK_BROWN)
arcade.draw_triangle_filled(630, 200, 770, 200, 700, 300, arcade.color.BRITISH_RACING_GREEN)
arcade.draw_triangle_filled(640, 250, 760, 250, 700, 325, arcade.color.BRITISH_RACING_GREEN)
arcade.draw_triangle_filled(650, 290, 750, 290, 700, 360, arcade.color.BRITISH_RACING_GREEN)

# Draw a tree.
arcade.draw_rectangle_filled(530, 225, 50, 150, arcade.color.DARK_BROWN)
arcade.draw_circle_filled(525, 300, 50, arcade.color.BRITISH_RACING_GREEN)
arcade.draw_circle_filled(555, 285, 40, arcade.color.BRITISH_RACING_GREEN)
arcade.draw_circle_filled(485, 330, 40, arcade.color.BRITISH_RACING_GREEN)
arcade.draw_circle_filled(505, 280, 40, arcade.color.BRITISH_RACING_GREEN)
arcade.draw_circle_filled(535, 360, 40, arcade.color.BRITISH_RACING_GREEN)
arcade.draw_circle_filled(560, 325, 40, arcade.color.BRITISH_RACING_GREEN)

# Draw apples for a tree.
arcade.draw_circle_filled(555, 345, 7, arcade.color.RED)
arcade.draw_circle_filled(485, 330, 7, arcade.color.RED)
arcade.draw_circle_filled(490, 275, 7, arcade.color.RED)
arcade.draw_circle_filled(525, 300, 7, arcade.color.RED)
arcade.draw_circle_filled(570, 268, 7, arcade.color.RED)

# Draw a sun.
arcade.draw_circle_filled(650, 500, 50, arcade.color.YELLOW)

arcade.finish_render()

arcade.run()