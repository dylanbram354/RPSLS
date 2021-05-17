from gesture import Gesture


class GestureOptions:
    def __init__(self):
        self.list = self.create_gesture_list()

    def create_gesture_list(self):
        rock = Gesture('ROCK', ['SCISSORS', 'LIZARD'], ['crushes', 'crushes'])
        scissors = Gesture('SCISSORS', ['PAPER', 'LIZARD'], ['cuts', 'decapitates'])
        paper = Gesture('PAPER', ['ROCK', 'SPOCK'], ['covers', 'disproves'])
        lizard = Gesture('LIZARD', ['SPOCK', 'PAPER'], ['poisons', 'eats'])
        spock = Gesture('SPOCK', ['SCISSORS', 'ROCK'], ['smashes', 'vaporizes'])

        gesture_list = [rock, paper, scissors, lizard, spock]

        return gesture_list
