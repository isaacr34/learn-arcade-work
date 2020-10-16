import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_GEM = 0.5
SPRITE_SCALING_COAL = 0.25
COAL_COUNT = 50
GEM_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Gem(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Coal(arcade.Sprite):

    def reset_pos(self):
        self.left = random.randrange(SCREEN_HEIGHT)
        self.center_x = SCREEN_WIDTH

    def update(self):
        self.center_x -= 1

        if self.right < 0:
            self.reset_pos()


class MyGame(arcade.Window):

    def __init__(self):

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.gem_list = None
        self.coal_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()
        self.coal_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character_maleAdventurer_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(GEM_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            gem = Gem("platformPack_item010.png", SPRITE_SCALING_GEM)

            # Position the coin
            gem.center_x = random.randrange(SCREEN_WIDTH)
            gem.center_y = random.randrange(SCREEN_HEIGHT)
            gem.change_x = random.randrange(-3, 4)
            gem.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.gem_list.append(gem)

        for i in range(COAL_COUNT):

            coal = Coal("ore_coal.png", SPRITE_SCALING_COAL)

            coal.center_x = random.randrange(SCREEN_WIDTH)
            coal.center_y = random.randrange(SCREEN_HEIGHT)

            self.coal_list.append(coal)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.gem_list.draw()
        self.player_list.draw()
        self.coal_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):

        self.gem_list.update()

        gems_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.gem_list)

        for gem in gems_hit_list:
            gem.remove_from_sprite_lists()
            self.score += 1

        self.coal_list.update()

        coal_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coal_list)

        for coal in coal_hit_list:
            coal.remove_from_sprite_lists()
            self.score -= 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
