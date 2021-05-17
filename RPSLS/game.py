from gesture import Gesture
from human import Human
from ai import AI
from gesture_options import GestureOptions


class Game:
    def __init__(self):
        self.player_one = ''
        self.player_two = ''
        self.score_to_win = 2

    def run_game(self):
        print("Welcome to the Rock, Paper, Scissors, Lizard, Spock! "
              "\nThe game works just like rock, paper, scissors, "
              "but each gesture beats two other gestures and loses to two other gestures. "
              "\nHere are all the gesture "
              "options and how they interact with each other: \n")
        self.display_gestures()
        ready_to_play = 'yes'
        while ready_to_play != 'no':
            ready_to_play = input("\nReady to play? (yes/no)")
            if ready_to_play == 'yes':
                self.select_players()
                self.select_score_to_win()
                print(f"\nLet's play!\n")
                while self.player_one.score < self.score_to_win and self.player_two.score < self.score_to_win:
                    self.game_round()
                if self.player_one.score == self.score_to_win:
                    print(f"\nGame over! {self.player_one.name} wins!")
                else:
                    print(f"\nGame over! {self.player_two.name} wins!")
                print("\nLet's play again, shall we?")
            elif ready_to_play == 'no':
                print('\nSee you next time!')
            else:
                print("Oops! Invalid input, try again...")



    def display_gestures(self):
        GestureOptions().create_gesture_list()
        gestures = GestureOptions().list
        i = 0
        while i < len(gestures):
            print(f"{gestures[i].name} {gestures[i].attack_words[0]} {gestures[i].beats[0]} and "
                  f"{gestures[i].attack_words[1]} {gestures[i].beats[1]}")
            i += 1


    def select_players(self):
        player_one = Human()
        player_one.choose_name()
        user_input = 'word'
        while user_input == 'word':
            user_input = input(f"Hello {player_one.name}! Would you like to play single-player or multiplayer? "
                               f"Enter '1' for single-player or '2' for multiplayer. ")
            if user_input == '1':
                print("You have selected single-player! You will play against an AI opponent.")
                player_two = AI()
            elif user_input == '2':
                print("You have selected multiplayer! Player two, please enter your name below. ")
                player_two = Human()
                player_two.choose_name()
            else:
                user_input = 'word'
                print("Oops! Invalid input. Try again... \n")
        self.player_one = player_one
        self.player_two = player_two

    def select_score_to_win(self):
        user_input = 'word'
        while user_input == 'word':
            user_input == input(f"Enter the number of rounds needed to win (enter '2' for best 2 out of 3, etc.). "
                                f"Maximum is 5.")
            if user_input > 5:
                print("That number is above the maximum allowed! Score to win has been set to 5.")
            elif 0 < user_input < 5:
                self.score_to_win = user_input
                print(f"Score to win has been set to {user_input}!")
            else:
                user_input = 'word'
                print("Oops! Invalid input. Try again...")

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
            attack_word_index = self.player_two.gesture.beats.index(self.player_one.gesture.name)
            attack_word = self.player_two.gesture.attack_words[attack_word_index]
            print(f"\n{self.player_two.gesture.name} {attack_word} {self.player_one.gesture.name}!\n"
                  f"{self.player_two.name} wins the round! ")
        else:
            self.player_one.score += 1
            attack_word_index = self.player_one.gesture.beats.index(self.player_two.gesture.name)
            attack_word = self.player_one.gesture.attack_words[attack_word_index]
            print(f"\n{self.player_one.gesture.name} {attack_word} {self.player_two.gesture.name}!\n"
                  f"{self.player_one.name} wins the round! ")
        print(f"\n{self.player_one.name} score: {self.player_one.score}\n"
              f"{self.player_two.name} score: {self.player_two.score}")



