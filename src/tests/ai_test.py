import unittest
import numpy as np
from game import Game
from ai import Ai


class TestAi(unittest.TestCase):
    def setUp(self):
        self.ai = Ai()

    def test_initialization(self):
        self.assertTrue(np.array_equal(self.ai.board, np.zeros((6, 7))))
        self.assertEqual(self.ai.player, 1)
        self.assertIsInstance(self.ai.game, Game)

    def test_make_move(self):
        board = np.zeros((6, 7))
        self.ai.make_move(board, 2, 1)
        self.assertEqual(board[5][2], 1)

    def test_is_winning_move(self):
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
