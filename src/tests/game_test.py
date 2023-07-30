import unittest
from game import Game

ROWS = 6
COLUMN = 7


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.board = Game.create_board()
