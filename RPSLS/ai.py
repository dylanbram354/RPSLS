from player import Player
from gesture_options import GestureOptions
import random


class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = 'AI'

    def throw_gesture(self):
        selection = random.choice(GestureOptions.list)
        return selection
