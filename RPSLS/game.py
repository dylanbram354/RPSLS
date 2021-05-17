from gesture import Gesture
from human import Human
from ai import AI
from gesture_options import GestureOptions


class Game:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.number_of_rounds = 0

    def game_setup(self):
        pass

    def display_gestures(self):
        pass

    def game_round(self):
        player_one_choice = 1
        player_two_choice = 1
        while player_two_choice == player_one_choice:
            player_one_choice = self.player_one.choose_gesture()
            player_two_choice = self.player_two.choose_gesture()
            if player_one_choice == player_two_choice:
                print(f"Oops! You both chose {player_one_choice.name}. Let's go again!")
            print(f"{self.player_one.name} chose {self.player_one.gesture.name}. {self.player_two.name} chose "
                  f"{self.player_two.gesture.name}.")
        if self.player_one.gesture.name in self.player_two.gesture.beats:
            self.player_two.score += 1
            print(f"{self.player_two.name} wins the round! ")
        else:
            self.player_one.score += 1
            print(f"{self.player_one.name} wins the round!")



