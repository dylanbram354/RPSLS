from gesture import Gesture


class GestureOptions:
    def __init__(self):
        self.list = self.create_gesture_list()

    def create_gesture_list(self):
        rock = Gesture('rock', ['scissors', 'lizard'])
        scissors = Gesture('scissors', ['paper', 'lizard'])
        paper = Gesture('paper', ['rock', 'Spock'])
        lizard = Gesture('lizard', ['Spock', 'paper'])
        spock = Gesture('Spock', ['scissors', 'rock'])

        gesture_list = [rock, paper, scissors, lizard, spock]

        return gesture_list
