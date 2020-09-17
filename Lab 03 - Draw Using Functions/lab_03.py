import arcade

arcade.open_window(800, 600, "Lab 2")

arcade.set_background_color(arcade.color.AZURE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 180, 0, arcade.color.BUD_GREEN)

def draw_house():
    """ Draw a house. """
    arcade.draw_lrtb_rectangle_filled(70, 400, 400, 150, arcade.color.CARROT_ORANGE)
    arcade.draw_triangle_filled(65, 400, 225, 500, 405, 400, arcade.color.BLACK)
    arcade.draw_rectangle_filled(225, 225, 100, 150, arcade.color.BLUE_SAPPHIRE)
    arcade.draw_circle_filled(255, 240, 7, arcade.color.BROWN)

def draw_tree():
    """ Draw a tree. """
    arcade.draw_rectangle_filled(700, 200, 60, 100, arcade.color.DARK_BROWN)
    arcade.draw_triangle_filled(630, 200, 770, 200, 700, 300, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_triangle_filled(640, 250, 760, 250, 700, 325, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_triangle_filled(650, 290, 750, 290, 700, 360, arcade.color.BRITISH_RACING_GREEN)

def draw_apple_tree():
    """ Draw an apple tree. """
    x = 480
    y = 250
    arcade.draw_rectangle_filled(530, 225, 50, 150, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(525, 300, 50, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_circle_filled(555, 285, 40, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_circle_filled(485, 330, 40, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_circle_filled(505, 280, 40, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_circle_filled(535, 360, 40, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_circle_filled(560, 325, 40, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_circle_filled(x + 80, y + 90, 7, arcade.color.RED)
    arcade.draw_circle_filled(x, y + 80, 7, arcade.color.RED)
    arcade.draw_circle_filled(x + 10, y + 30, 7, arcade.color.RED)
    arcade.draw_circle_filled(x + 50, y + 50, 7, arcade.color.RED)
    arcade.draw_circle_filled(x +85, y + 30, 7, arcade.color.RED)

def draw_sun():
    """ Draw a sun. """
    arcade.draw_circle_filled(650, 500, 50, arcade.color.YELLOW)

draw_house()
draw_tree()
draw_apple_tree()
draw_sun()

arcade.finish_render()

arcade.run()