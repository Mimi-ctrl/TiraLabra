import unittest
from game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_vertical_win(self):
        self.game.drop_piece(0, 1)
        self.game.drop_piece(0, 1)
        self.game.drop_piece(0, 1)
        self.game.drop_piece(0, 1)
        self.assertEqual(self.game.check_win(), True)

    def test_horizontal_win(self):
        self.game.drop_piece(0, 1)
        self.game.drop_piece(1, 1)
        self.game.drop_piece(2, 1)
        self.game.drop_piece(3, 1)
        self.assertEqual(self.game.check_win(), True)

    def test_positive_diagonal_win(self):
        self.game.drop_piece(0, 1)
        self.game.drop_piece(1, 1)
        self.game.drop_piece(1, 1)
        self.game.drop_piece(2, 1)
        self.game.drop_piece(2, 1)
        self.game.drop_piece(2, 1)
        self.game.drop_piece(3, 1)
        self.game.drop_piece(3, 1)
        self.game.drop_piece(3, 1)
        self.game.drop_piece(3, 1)
        self.assertEqual(self.game.check_win(), True)

    def test_negative_diagonal_win(self):
        self.game.drop_piece(0, 1)
        self.game.drop_piece(0, 1)
        self.game.drop_piece(0, 1)
        self.game.drop_piece(0, 1)
        self.game.drop_piece(1, 1)
        self.game.drop_piece(1, 1)
        self.game.drop_piece(1, 1)
        self.game.drop_piece(2, 1)
        self.game.drop_piece(2, 1)
        self.game.drop_piece(3, 1)
        self.assertEqual(self.game.check_win(), True)
