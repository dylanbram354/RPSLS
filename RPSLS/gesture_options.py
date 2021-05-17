from gesture import Gesture


class GestureOptions:
    def __init__(self):
        self.list = self.create_gesture_list()

    def create_gesture_list(self):
        rock = Gesture('rock', ['scissors', 'lizard'], ['crushes', 'crushes'])
        scissors = Gesture('scissors', ['paper', 'lizard'], ['cuts', 'decapitates'])
        paper = Gesture('paper', ['rock', 'Spock'], ['covers', 'disproves'])
        lizard = Gesture('lizard', ['Spock', 'paper'], ['poisons', 'eats'])
        spock = Gesture('Spock', ['scissors', 'rock'], ['smashes', 'vaporizes'])

        gesture_list = [rock, paper, scissors, lizard, spock]

        return gesture_list
