from player import Player
from gesture_options import GestureOptions
from getpass import getpass


class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_name(self):
        self.name = input("Enter your name: ")

    def choose_gesture(self):
        gesture = ''
        while gesture == '':
            user_choice = input(f"\n{self.name}, choose a gesture to throw! ")
            user_choice = user_choice.upper()
            i = 0
            while i < len(GestureOptions().list):
                if user_choice == GestureOptions().list[i].name:
                    gesture = GestureOptions().list[i]
                i += 1
            if gesture == '':
                print("\nOops! Invalid input. Try again...")
        self.gesture = gesture
        return gesture





