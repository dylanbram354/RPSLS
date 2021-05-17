from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_name(self):
        self.name = input("Enter your name ")

    def choose_gesture(self):
        pass


