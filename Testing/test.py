import arcade
import random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


class Coin(arcade.Sprite):

    def reset(selfself):
        self.bottom = SCREEN_HEIGHT
