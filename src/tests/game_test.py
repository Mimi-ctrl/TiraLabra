import unittest
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    
    def test_create_board(self):
        self.game.create_board()


        