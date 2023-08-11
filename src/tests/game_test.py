import unittest
import numpy as np
from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_is_valid_column_valid(self):
        self.assertTrue(self.game.is_valid_column(self.game.board, 0))
        self.assertTrue(self.game.is_valid_column(self.game.board, 6))

    def test_is_valid_column_invalid(self):
        self.assertFalse(self.game.is_valid_column(self.game.board, -1))
        self.assertFalse(self.game.is_valid_column(self.game.board, 7))
        self.assertFalse(self.game.is_valid_column(self.game.board, 10))

    def test_drop_piece_valid(self):
        board = np.array([[0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0]])
        self.assertTrue(self.game.drop_piece(board, 0, 2))
        self.assertTrue(self.game.drop_piece(board, 1, 1))
        self.assertTrue(self.game.drop_piece(board, 2, 2))
        self.assertTrue(self.game.drop_piece(board, 3, 1))
        self.assertTrue(self.game.drop_piece(board, 4, 2))
        self.assertTrue(self.game.drop_piece(board, 5, 1))
        self.assertTrue(self.game.drop_piece(board, 6, 2))

    def test_drop_piece_invalid(self):
        board = np.array([[1, 2, 1, 2, 1, 2, 1],
                          [2, 1, 2, 1, 2, 1, 2],
                          [1, 2, 1, 2, 1, 2, 1],
                          [2, 1, 2, 1, 2, 1, 2],
                          [1, 2, 1, 2, 1, 2, 1],
                          [2, 1, 2, 1, 2, 1, 2]])
        self.assertFalse(self.game.drop_piece(board, 0, 1))
        self.assertFalse(self.game.drop_piece(board, 10, 1))

    def test_check_is_board_full_full(self):
        board = np.array([[1, 2, 1, 2, 1, 2, 1],
                          [2, 1, 2, 1, 2, 1, 2],
                          [1, 2, 1, 2, 1, 2, 1],
                          [2, 1, 2, 1, 2, 1, 2],
                          [1, 2, 1, 2, 1, 2, 1],
                          [2, 1, 2, 1, 2, 1, 2]])
        self.assertTrue(self.game.check_is_board_full(board))

    def test_check_is_board_full_not_full(self):
        board = np.array([[0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0]])
        self.assertFalse(self.game.check_is_board_full(board))

    def test_horizontal_win(self):
        board = np.array([[0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [1, 1, 1, 1, 0, 0, 0]])
        self.game.board = board
        self.assertTrue(self.game.check_win(self.game.board))

    def test_vertical_win(self):
        board = np.array([[0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0]])
        self.game.board = board
        self.assertTrue(self.game.check_win(self.game.board))

    def test_positive_diagonal_win(self):
        board = np.array([[0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1],
                          [0, 0, 0, 0, 0, 1, 0],
                          [0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0]])
        self.game.board = board
        self.assertTrue(self.game.check_win(self.game.board))

    def test_negative_diagonal_win(self):
        board = np.array([[0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 1, 0]])
        self.game.board = board
        self.assertTrue(self.game.check_win(self.game.board))
