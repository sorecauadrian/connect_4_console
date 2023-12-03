from texttable import Texttable

class ColumnNotAvailableError(Exception):
    pass


class ColumnNotExistingError(Exception):
    pass


class Board:
    def __init__(self, rows : int = 6, columns : int = 7):
        self._rows = rows
        self._columns = columns
        self._data = [[' ' for _ in range(columns)] for _ in range(rows)]

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    @property
    def data(self):
        return self._data

    def on_board(self, column : int):
        return 0 <= column < self._columns

    def is_occupied(self, row : int, column : int):
        """
        checks if a certain spot is occupied
        """
        return self.data[row][column] == 'C' or self.data[row][column] == 'P'

    def game_won(self):
        """
        checks if the game is won
        returns the circle of the winner if the game is won and False otherwise
        """
        for row in range(self._rows - 3):
            for column in range(self._columns):
                if self.data[row][column] == self.data[row + 1][column] == self.data[row + 2][column] == self.data[row + 3][column] and self.is_occupied(row, column):
                    return self.data[row][column]

        for row in range(self._rows):
            for column in range(self.columns - 3):
                if self.data[row][column] == self.data[row][column + 1] == self.data[row][column + 2] == self.data[row][column + 3] and self.is_occupied(row, column):
                    return self.data[row][column]

        for row in range(self.rows - 3):
            for column in range(self.columns - 3):
                if self.data[row][column] == self.data[row + 1][column + 1] == self.data[row + 2][column + 2] == self.data[row + 3][column + 3] and self.is_occupied(row, column):
                    return self.data[row][column]

        for row in range(self.rows - 3):
            for column in range(self.columns - 1, 3, -1):
                if self.data[row][column] == self.data[row + 1][column - 1] == self.data[row + 2][column - 2] == self.data[row + 3][column - 3] and self.is_occupied(row, column):
                    return self.data[row][column]

        return False

    def game_draw(self):
        """
        checks if the game is a draw
        returns True if the game is a draw and False otherwise
        """
        for row in range(self._rows):
            for column in range(self._columns):
                if self.data[row][column] == ' ':
                    return False
        return True

    def is_legal_move(self, column : int):
        """
        checks if the move is legal for a given state of a board and a column
        returns True if the move is legal and False otherwise
        """
        if self.on_board(column):
            for i in range(self.rows - 1, -1, -1):
                if self.data[i][column] == ' ':
                    return True
            return False
        raise ColumnNotExistingError("this column does not exist!")

    def move(self, circle : str, column : int):
        """
        if possible, makes a move and returns True
        otherwise it throws an error
        """
        if self.is_legal_move(column):
            for i in range(self.rows - 1, -1, -1):
                if self.data[i][column] == ' ':
                    self._data[i][column] = circle
                    return True
        raise ColumnNotAvailableError("column is full! try again!")

    def simulate_move(self, circle : str, given_column : int):
        simulated_board = Board(self.rows, self.columns)
        for row in range(simulated_board.rows):
            for column in range(simulated_board.columns):
                simulated_board._data[row][column] = self.data[row][column]
        if simulated_board.move(circle, given_column):
            return simulated_board
        return False

    def __str__(self):
        """
        draws the board
        """
        board_representation = Texttable()

        board_representation.header([i for i in range(self._columns)])
        for row in self._data:
            board_representation.add_row(row)

        return board_representation.draw()
