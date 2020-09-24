import arcade


def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, 800, 180, 0, arcade.color.BUD_GREEN)


def draw_house(x, y):
    """ Draw a house. """
    arcade.draw_point(x, y, arcade.color.RED, 5)

    arcade.draw_lrtb_rectangle_filled(x - 55, y + 170, 400, 150, arcade.color.CARROT_ORANGE)
    arcade.draw_triangle_filled(x - 60, y + 170, 225, 500, 405, 400, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x + 100, y - 5, 100, 150, arcade.color.BLUE_SAPPHIRE)
    arcade.draw_circle_filled(x + 130, y + 10, 7, arcade.color.BROWN)


def draw_tree(x, y):
    """ Draw a tree. """
    arcade.draw_point(x, y, arcade.color.RED, 5)

    arcade.draw_rectangle_filled(x + 100, y, 60, 100, arcade.color.DARK_BROWN)
    arcade.draw_triangle_filled(x + 30, y, 770, 200, 700, 300, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_triangle_filled(x + 40, y + 50, 760, 250, 700, 325, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_triangle_filled(x + 50, y + 90, 750, 290, 700, 360, arcade.color.BRITISH_RACING_GREEN)


def draw_apple_tree(x, y):
    """ Draw an apple tree. """
    arcade.draw_point(x, y, arcade.color.RED, 5)

    arcade.draw_rectangle_filled(x + 50, y - 25, 50, 150, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(x + 45, y + 50, 50, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_circle_filled(x + 75, y + 35, 40, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_circle_filled(x + 5, y + 80, 40, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_circle_filled(x + 25, y + 30, 40, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_circle_filled(x + 55, y + 110, 40, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_circle_filled(x + 80, y + 75, 40, arcade.color.BRITISH_RACING_GREEN)
    arcade.draw_circle_filled(x + 80, y + 90, 7, arcade.color.RED)
    arcade.draw_circle_filled(x, y + 80, 7, arcade.color.RED)
    arcade.draw_circle_filled(x + 10, y + 30, 7, arcade.color.RED)
    arcade.draw_circle_filled(x + 50, y + 50, 7, arcade.color.RED)
    arcade.draw_circle_filled(x + 85, y + 30, 7, arcade.color.RED)


def draw_sun(x, y):
    """ Draw a sun. """
    arcade.draw_point(x, y, arcade.color.RED, 5)

    arcade.draw_circle_filled(x, y, 50, arcade.color.YELLOW)


def main():
    arcade.open_window(800, 600, "Lab 2")
    arcade.set_background_color(arcade.color.AZURE)
    arcade.start_render()

    draw_grass()
    draw_house(125, 230)
    draw_tree(600, 200)
    draw_apple_tree(480, 250)
    draw_sun(650, 500)

    arcade.finish_render()
    arcade.run()


main()
