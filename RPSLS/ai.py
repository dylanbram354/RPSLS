from player import Player
from gesture_options import GestureOptions
import random


class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = 'AI'

    def choose_gesture(self):
        print("AI's turn. Selecting gesture to throw...")
        gesture = random.choice(GestureOptions().list)
        self.gesture = gesture
        return gesture
