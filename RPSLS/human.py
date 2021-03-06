from player import Player
from gesture_options import GestureOptions
from getpass import getpass


class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_name(self):
        self.name = input("\nEnter your name: ")

    def choose_gesture(self):
        gesture = ''
        while gesture == '':
            user_choice = getpass(f"\n{self.name}, choose a gesture to throw! ") ##why does this get weird whenever AI wins round?
            user_choice = user_choice.upper()
            for element in GestureOptions().list:
                if user_choice == element.name:
                    gesture = element
            if gesture == '':
                print("\nOops! Invalid input. Try again...")
        self.gesture = gesture
        return gesture





