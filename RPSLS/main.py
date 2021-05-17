from ai import AI
from human import Human
from game import Game

if __name__ == '__main__':
    human = Human()
    human.choose_name()
    ai = AI()
    game_test = Game(human, ai)
    game_test.number_of_rounds = 2
    game_test.game_round()
    print(game_test.player_one.score)
    print(game_test.player_two.score)