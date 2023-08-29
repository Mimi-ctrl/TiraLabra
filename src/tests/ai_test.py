from io import StringIO
import unittest
from unittest.mock import patch
import numpy as np
from game import Game
from ai import Ai


class TestAi(unittest.TestCase):
    def setUp(self):
        self.ai = Ai()
        self.game = Game()

    def test_initialization(self):
        self.assertTrue(np.array_equal(self.ai.board, np.zeros((6, 7))))
        self.assertEqual(self.ai.player, 1)
        self.assertIsInstance(self.ai.game, Game)

    def test_make_move(self):
        board = np.zeros((6, 7))
        self.ai.make_move(board, 2, 1)
        self.assertEqual(board[5][2], 1)

    def test_is_winning_move_horizontal(self):
        board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])
        self.assertTrue(self.ai.is_winning_move(board, 1))
        self.assertFalse(self.ai.is_winning_move(board, 2))

    def test_is_winning_move_vertical(self):
        board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0]
        ])
        self.assertTrue(self.ai.is_winning_move(board, 1))
        self.assertFalse(self.ai.is_winning_move(board, 2))

    def test_is_winning_move_diagonal(self):
        board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0]
        ])
        self.assertTrue(self.ai.is_winning_move(board, 1))
        self.assertFalse(self.ai.is_winning_move(board, 2))

    def test_is_winning_move_diagonal_increasing(self):
        board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0]
        ])
        self.assertTrue(self.ai.is_winning_move(board, 1))
        self.assertFalse(self.ai.is_winning_move(board, 2))

    def test_evaluate_line(self):
        line = [1, 1, 1, 0]
        self.assertEqual(self.ai.evaluate_line(line, 1), 5)
        self.assertEqual(self.ai.evaluate_line(line, 2), -4)
        line = [1, 1, 1, 1]
        self.assertEqual(self.ai.evaluate_line(line, 1), 100)
        line = [1, 1, 0, 0]
        self.assertEqual(self.ai.evaluate_line(line, 1), 2)

    def test_find_best_move(self):
        board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 2, 0],
            [0, 0, 0, 0, 1, 2, 0]
        ])
        self.ai.board = board.copy()
        best_move = self.ai.find_best_move(board)
        self.assertEqual(best_move, 5)

    def test_minimax(self):
        board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 2, 0],
            [0, 0, 0, 0, 1, 2, 0]
        ])
        score = self.ai.minimax(board, 4, -10**9, 10**9, True)
        self.assertIsInstance(score, int)

    def test_game_loop(self):
        with self.assertRaises(OSError):
            self.ai.game_loop()

    def test_drop_piece(self):
        self.game.drop_piece(self.ai.board, 0, 1)
        self.assertEqual(self.ai.board[5][0], 1)

    def test_check_win(self):
        self.ai.board[5][0] = 1
        self.ai.board[5][1] = 1
        self.ai.board[5][2] = 1
        self.ai.board[5][3] = 1
        self.assertTrue(self.game.check_win(self.ai.board))

    def test_find_best_move_another_case(self):
        board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 2, 1, 2, 0],
            [0, 0, 2, 1, 2, 1, 0]
        ])
        self.ai.board = board.copy()
        best_move = self.ai.find_best_move(board)
        self.assertEqual(best_move, 4)

    def test_find_best_move_yet_another_case(self):
        board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 2, 0, 0, 0],
            [0, 0, 2, 1, 0, 0, 0],
            [0, 0, 1, 2, 0, 0, 0]
        ])
        self.ai.board = board.copy()
        best_move = self.ai.find_best_move(board)
        self.assertEqual(best_move, 2)

    def test_find_best_move_different_configuration(self):
        board = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0]
        ])
        self.ai.board = board.copy()
        best_move = self.ai.find_best_move(board)
        self.assertEqual(best_move, 3)

    def test_init(self):
        self.assertTrue(np.array_equal(self.ai.board, np.zeros((6, 7))))
        self.assertEqual(self.ai.player, 1)
        self.assertIsNotNone(self.ai.game)

    @patch('builtins.input', side_effect=['0', '1', '0', '1', '0', '1', '0', '1', '0', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_loop_valid_input(self, mock_stdout, mock_input):
        self.ai.game_loop()
        output = mock_stdout.getvalue().strip()
        print("Final Output:\n", output)
        self.assertNotIn("Invalid column.", output)
        self.assertIn("Player  2 wins!", output)

    @patch('builtins.input', side_effect=['0', '1', '2', '3', '4', '5', '6'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_loop_draw(self, mock_stdout, mock_input):
        self.ai.board = np.ones((6, 7))
        self.ai.game_loop()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Draw match", output)