import unittest
import numpy as np
from unittest.mock import patch
from io import StringIO
from game import Game
from ai import Ai


class TestAi(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.ai = Ai()
        self.mock_input = patch("builtins.input", side_effect=["0"])
        self.mock_input.start()

    def test_is_winning_move(self):
        board = np.zeros((6, 7))
        for col in range(4):
            board[0][col] = 1
        self.assertTrue(self.ai.is_winning_move(board, 1))

    def test_four_in_a_row(self):
        line = [2, 2, 2, 2, 0]
        player = 2
        self.assertEqual(self.ai.evaluate_line(line, player), 100)

    def test_no_match(self):
        line = [1, 2, 1, 0, 0]
        player = 2
        self.assertEqual(self.ai.evaluate_line(line, player), 0)

    def tearDown(self):
        self.mock_input.stop()

    def test_make_move(self):
        board = np.zeros((6, 7))
        player = 1
        self.ai.make_move(board, 0, player)
        self.assertEqual(board[5][0], player)
