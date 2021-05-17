from gesture import Gesture
from human import Human
from ai import AI
from gesture_options import GestureOptions


class Game:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    def display_welcome(self):
        pass

    def display_gestures(self):
        pass

    def game_round(self):
        player_one_choice = 1
        player_two_choice = 0
        while player_two_choice != player_one_choice:
            player_one_choice = self.player_one.choose_gesture
            player_two_choice = self.player_two.choose_gesture


