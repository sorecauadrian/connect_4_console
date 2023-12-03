import unittest

from board.board import Board
from game.game import Player, AI, AI_level_1, AI_level_2


class Test(unittest.TestCase):
    def test_board(self):
        board = Board()
        self.assertEqual(board.rows, 6)
        self.assertEqual(board.columns, 7)
        self.assertEqual(board.on_board(0), True)
        self.assertEqual(board.on_board(6), True)
        self.assertEqual(board.on_board(7), False)
        self.assertEqual(board.game_won(), False)
        self.assertEqual(board.game_draw(), False)
        board.move("C", 0)
        board.move("C", 0)
        board.move("C", 0)
        board.move("C", 0)
        self.assertEqual(board.game_won(), "C")

    def test_player(self):
        player = Player()
        self.assertEqual(player.name, "adi")
        self.assertEqual(player.circle, "P")
        player.name = "laura"
        self.assertEqual(player.name, "laura")

    def test_ai(self):
        ai = AI()
        self.assertEqual(ai.circle, "C")

        board1 = Board()

        ai1 = AI_level_1()
        for _ in range(4):
            ai1.play(board1)
        self.assertEqual(board1.game_won(), ai1.circle)

        board2 = Board()
        ai2 = AI_level_2()
        for _ in range(19):
            ai2.play(board2)
        self.assertEqual(board2.game_won(), ai2.circle)
