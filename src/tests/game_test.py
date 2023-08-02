import unittest
from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_is_valid_column(self):
        self.assertTrue(self.game.is_valid_column(0))
        self.assertFalse(self.game.is_valid_column(7))
        self.game.board[0][0] = 1
        self.game.board[1][0] = 2
        self.game.board[2][0] = 1
        self.game.board[3][0] = 2
        self.game.board[4][0] = 1
        self.game.board[5][0] = 2
        self.assertFalse(self.game.is_valid_column(0))

    def test_drop_piece(self):
        self.assertTrue(self.game.drop_piece(0, 1))
        self.assertFalse(self.game.drop_piece(7, 2))
        self.game.board[0][1] = 1
        self.game.board[1][1] = 2
        self.game.board[2][1] = 1
        self.game.board[3][1] = 2
        self.game.board[4][1] = 1
        self.game.board[5][1] = 2
        self.assertFalse(self.game.drop_piece(1, 1))

    def test_horizontal_win(self):
        self.game.board[0][0] = 1
        self.game.board[0][1] = 1
        self.game.board[0][2] = 1
        self.game.board[0][3] = 1
        self.assertTrue(self.game.check_win())

    def test_vertical_win(self):
        self.game.board[0][0] = 2
        self.game.board[1][0] = 2
        self.game.board[2][0] = 2
        self.game.board[3][0] = 2
        self.assertTrue(self.game.check_win())

    def test_positive_diagonal_win(self):
        self.game.board[0][0] = 1
        self.game.board[1][1] = 1
        self.game.board[2][2] = 1
        self.game.board[3][3] = 1
        self.assertTrue(self.game.check_win())

    def test_negative_diagonal_win(self):
        self.game.board[0][3] = 2
        self.game.board[1][2] = 2
        self.game.board[2][1] = 2
        self.game.board[3][0] = 2
        self.assertTrue(self.game.check_win())

    def test_check_no_win(self):
        self.game.board[0][3] = 1
        self.game.board[1][2] = 2
        self.game.board[2][1] = 1
        self.game.board[3][0] = 2
        self.assertFalse(self.game.check_win())
