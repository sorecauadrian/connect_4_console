from board.board import Board, ColumnNotAvailableError, ColumnNotExistingError
from game.game import Player, AI, AI_level_1, AI_level_2, AI_level_3

class UI:
    def __init__(self, board : Board = None, player : Player = None, ai : AI = None):
        if board is None:
            board = Board()
        if player is None:
            player = Player()
        if ai is None:
            ai = AI_level_1()
        self._board = board
        self._player = player
        self._ai = ai

    @property
    def ai(self):
        return self._ai

    @ai.setter
    def ai(self, new_ai):
        self.ai = new_ai

    def set_player_name(self):
        player_name = input("your name: ")
        self._player.name = player_name

    @staticmethod
    def print_difficulties():
        print("\ndifficulties")
        print("1. very easy")
        print("2. easy")
        print("3. medium")
        print("0. exit")

    def select_difficulty(self):
        self.print_difficulties()
        choice = input("> ")
        if choice == "1":
            self._ai = AI_level_1()
        elif choice == "2":
            self._ai = AI_level_2()
        elif choice == "3":
            self._ai = AI_level_3()
        elif choice == "0":
            exit()
        else:
            print("invalid choice! you'll play against the 'very easy' computer!")

    def print_starting_description(self):
        print("\nconnect 4")
        print("---------")
        print(self._player)
        print(self._ai)
        print("---------")

    def start(self):
        self.set_player_name()
        self.select_difficulty()
        self.print_starting_description()
        turns = True
        print(self._board)
        while True:
            winner = self._board.game_won()
            if winner is not False:
                if winner == "C":
                    print("computer won!")
                else:
                    print(self._board)
                    print(self._player.name + " won!")
                exit()
            elif self._board.game_draw():
                if not turns:
                    print(self._board)
                print("draw!")
                exit()
            else:
                if turns:
                    choice = input("column: ")
                    if choice.isdigit():
                        try:
                            self._board.move(self._player.circle, int(choice))
                            turns = not turns
                        except ColumnNotAvailableError as e:
                            print(e)
                        except ColumnNotExistingError as e:
                            print(e)
                    else:
                        print("column must be an integer! try again")
                else:
                    self._ai.play(self._board)
                    turns = not turns
                    print(self._board)


