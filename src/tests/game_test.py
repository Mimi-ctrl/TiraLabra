import unittest
from game import Game


class TestGame(unittest.TestCase):

    def test_vertical_win(self):
        game = Game()
        game.drop_piece(0, 1)
        game.drop_piece(0, 1)
        game.drop_piece(0, 1)
        game.drop_piece(0, 1)
        self.assertEqual(game.check_win(), True)

    def test_no_win(self):
        game = Game()
        game.drop_piece(0, 2)
        game.drop_piece(1, 1)
        game.drop_piece(2, 1)
        game.drop_piece(0, 2)
        self.assertEqual(game.check_win(), None)

    def test_horizontal_win(self):
        game = Game()
        game.drop_piece(0, 1)
        game.drop_piece(1, 1)
        game.drop_piece(2, 1)
        game.drop_piece(3, 1)
        self.assertEqual(game.check_win(), True)

    def test_positive_diagonal_win(self):
        game = Game()
        game.drop_piece(0, 1)
        game.drop_piece(1, 1)
        game.drop_piece(1, 1)
        game.drop_piece(2, 1)
        game.drop_piece(2, 1)
        game.drop_piece(2, 1)
        game.drop_piece(3, 1)
        game.drop_piece(3, 1)
        game.drop_piece(3, 1)
        game.drop_piece(3, 1)
        self.assertEqual(game.check_win(), True)

    def test_negative_diagonal_win(self):
        game = Game()
        game.drop_piece(0, 1)
        game.drop_piece(0, 1)
        game.drop_piece(0, 1)
        game.drop_piece(0, 1)
        game.drop_piece(1, 1)
        game.drop_piece(1, 1)
        game.drop_piece(1, 1)
        game.drop_piece(2, 1)
        game.drop_piece(2, 1)
        game.drop_piece(3, 1)
        self.assertEqual(game.check_win(), True)
