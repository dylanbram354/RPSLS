from player import Player
from gesture_options import GestureOptions
from getpass import getpass


class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_name(self):
        self.name = input("Enter your name: ")

    def choose_gesture(self):
        user_choice = getpass(f"{self.name}'s turn. Choose a gesture to throw! ")
        gesture = ''
        while gesture == '':
            i = 0
            while i < len(GestureOptions().list):
                if user_choice == GestureOptions().list[i].name:
                    gesture = GestureOptions().list[i]
                i += 1
            if gesture == '':
                print("Oops! Invalid input. Try again...")
        self.gesture = gesture
        return gesture





