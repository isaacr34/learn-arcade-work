import arcade

WIDTH = 50
HEIGHT = 50
MARGIN = 5
ROW_COUNT = 10
COLUMN_COUNT = 10

SCREEN_HEIGHT = (HEIGHT * ROW_COUNT + MARGIN * (ROW_COUNT + 1))
SCREEN_WIDTH = (WIDTH * COLUMN_COUNT + MARGIN * (COLUMN_COUNT + 1))


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        print(self.grid)

        self.grid = [[0 for x in range(10)] for y in range(10)]

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        for column in range (COLUMN_COUNT):
            for row in range (ROW_COUNT):
                arcade.draw_rectangle_filled((WIDTH / 2) + (column * (WIDTH + MARGIN)) + MARGIN,
                                             (HEIGHT / 2) + (row * (HEIGHT + MARGIN)) + MARGIN,
                                             WIDTH, HEIGHT, arcade.color.WHITE)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
