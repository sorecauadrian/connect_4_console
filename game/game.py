import random

from board.board import Board

class Player:
    def __init__(self, name : str = "adi", circle : str = "P"):
        self._name = name
        self._circle = circle

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def circle(self):
        return self._circle

    def __str__(self):
        return self.name + " is playing with " + self.circle

class AI:
    def __init__(self, circle = "C", opponent_circle = "P"):
        self._circle = circle
        self._opponent_circle = opponent_circle

    @property
    def circle(self):
        return self._circle

    @property
    def opponent_circle(self):
        return self._opponent_circle

    def __str__(self):
        return "the computer is playing with " + self.circle

class AI_level_1(AI):
    def play(self, board : Board):
        for column in range(board.columns):
            if board.is_legal_move(column):
                board.move(self.circle, column)
                return True

class AI_level_2(AI):
    def play(self, board : Board):
        available_columns = []
        for column in range(board.columns):
            if board.is_legal_move(column):
                available_columns.append(column)
        board.move(self.circle, available_columns[random.randint(0, len(available_columns) - 1)])
        return True

class AI_level_3(AI):
    def play(self, board : Board):
        available_columns = []
        for column in range(board.columns):
            if board.is_legal_move(column):
                available_columns.append(column)
        for column in available_columns:
            if board.simulate_move(self.circle, column).game_won() or board.simulate_move(self._opponent_circle, column).game_won():
                board.move(self.circle, column)
                return True
        board.move(self.circle, available_columns[random.randint(0, len(available_columns) - 1)])
        return True
