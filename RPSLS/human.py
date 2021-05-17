from player import Player
from gesture_options import GestureOptions
import getpass

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_name(self):
        self.name = input("Enter your name ")

    def throw_gesture(self):
        choice = getpass.getpass('Choose a gesture to throw! ')
        print(choice)



