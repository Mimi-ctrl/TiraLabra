from io import StringIO
import unittest
from unittest.mock import patch
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
        self.assertFalse(self.game.drop_piece(board, -4, 1))

    def test_check_is_board_full_full(self):
        board = np.array([[1, 2, 1, 2, 1, 2, 1],
                          [2, 1, 2, 1, 2, 1, 2],
                          [1, 2, 1, 2, 1, 2, 1],
                          [2, 1, 2, 1, 2, 1, 2],
                          [1, 2, 1, 2, 1, 2, 1],
                          [2, 1, 2, 1, 2, 1, 2]])
        self.assertTrue(self.game.check_is_board_full(board))

    def test_check_is_board_full_not_full(self):
        self.game.drop_piece(self.game.board, 0, 1)
        self.game.drop_piece(self.game.board, 0, 1)
        self.game.drop_piece(self.game.board, 0, 1)
        self.assertFalse(self.game.check_is_board_full(self.game.board))

    def test_vertical_win(self):
        self.game.drop_piece(self.game.board, 0, 1)
        self.game.drop_piece(self.game.board, 0, 1)
        self.game.drop_piece(self.game.board, 0, 1)
        self.game.drop_piece(self.game.board, 0, 1)
        self.assertEqual(self.game.check_win(self.game.board), True)

    def test_vertical_win_2(self):
        self.game.drop_piece(self.game.board, 1, 1)
        self.game.drop_piece(self.game.board, 1, 1)
        self.game.drop_piece(self.game.board, 1, 1)
        self.game.drop_piece(self.game.board, 1, 1)
        self.assertEqual(self.game.check_win(self.game.board), True)

    def test_horizontal_win(self):
        self.game.drop_piece(self.game.board, 0, 1)
        self.game.drop_piece(self.game.board, 1, 1)
        self.game.drop_piece(self.game.board, 2, 1)
        self.game.drop_piece(self.game.board, 3, 1)
        self.assertEqual(self.game.check_win(self.game.board), True)

    def test_positive_diagonal_win(self):
        self.game.drop_piece(self.game.board, 0, 1)
        self.game.drop_piece(self.game.board, 1, 1)
        self.game.drop_piece(self.game.board, 1, 1)
        self.game.drop_piece(self.game.board, 2, 1)
        self.game.drop_piece(self.game.board, 2, 1)
        self.game.drop_piece(self.game.board, 2, 1)
        self.game.drop_piece(self.game.board, 3, 1)
        self.game.drop_piece(self.game.board, 3, 1)
        self.game.drop_piece(self.game.board, 3, 1)
        self.game.drop_piece(self.game.board, 3, 1)
        self.assertEqual(self.game.check_win(self.game.board), True)

    def test_drop_piece_invalid_column(self):
        board = np.zeros((6, 7))
        result = self.game.drop_piece(board, 10, 1)
        self.assertEqual(result, False)

    def test_negative_diagonal_win(self):
        self.game.drop_piece(self.game.board, 0, 1)
        self.game.drop_piece(self.game.board, 0, 1)
        self.game.drop_piece(self.game.board, 0, 1)
        self.game.drop_piece(self.game.board, 0, 1)
        self.game.drop_piece(self.game.board, 1, 1)
        self.game.drop_piece(self.game.board, 1, 1)
        self.game.drop_piece(self.game.board, 1, 1)
        self.game.drop_piece(self.game.board, 2, 1)
        self.game.drop_piece(self.game.board, 2, 1)
        self.game.drop_piece(self.game.board, 3, 1)
        self.assertEqual(self.game.check_win(self.game.board), True)

    def test_not_win_0(self):
        self.game.drop_piece(self.game.board, 6, 1)
        self.game.drop_piece(self.game.board, 6, 1)
        self.assertEqual(self.game.check_win(self.game.board), None)

    def test_not_win_1(self):
        self.game.drop_piece(self.game.board, 0, 3)
        self.game.drop_piece(self.game.board, 0, 4)
        self.assertEqual(self.game.check_win(self.game.board), None)

    def test_not_win_2(self):
        board = np.array([[]])
        self.assertEqual(self.game.check_win(board), None)

    @patch('builtins.input', side_effect=['0', '1', '2', '3', '4', '5', '6'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_loop_draw(self, mock_stdout, mock_input):
        self.game.board = np.ones((6, 7))
        self.game.game_loop()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Draw match", output)

    def test_drop_piece_valid_column(self):
        board = np.zeros((6, 7))
        self.assertTrue(self.game.drop_piece(board, 0, 1))
        self.assertEqual(board[5][0], 1)

    def test_check_win_positive_diagonal_1(self):
        board = np.zeros((6, 7))
        board[2][2] = 1
        board[3][3] = 1
        board[4][4] = 1
        board[5][5] = 1
        self.assertTrue(self.game.check_win(board))

    def test_check_win_negative_diagonal_1(self):
        board = np.zeros((6, 7))
        board[2][5] = 1
        board[3][4] = 1
        board[4][3] = 1
        board[5][2] = 1
        self.assertTrue(self.game.check_win(board))

    @patch('builtins.input', side_effect=['0', '1', '0', '1', '0', '1', '0', '1', '0', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_loop_valid_input(self, mock_stdout, mock_input):
        self.game.game_loop()
        output = mock_stdout.getvalue().strip()
        print("Final Output:\n", output)
        self.assertNotIn("Invalid column.", output)
        self.assertIn("Player  1 wins!", output)
