import unittest
import numpy as np
from unittest.mock import patch, MagicMock
from ai import Ai


class TestAi(unittest.TestCase):
    def setUp(self):
        self.ai = Ai()

    def test_is_winning_move(self):
        board = np.zeros((6, 7))
        for col in range(4):
            board[0][col] = 1
        self.assertTrue(self.ai.is_winning_move(board, 1))

    def test_evaluate_position(self):
        board = np.zeros((6, 7))
        board[0][3] = 1
        board[1][3] = 1
        board[2][3] = 1
        self.assertEqual(self.ai.evaluate_position(board, 1), 7)
