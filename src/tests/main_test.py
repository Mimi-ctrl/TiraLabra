import unittest
from unittest.mock import patch
from main import main


class TestMain(unittest.TestCase):

    @patch('menu.Menu.print_menu', return_value=True)
    @patch('menu.Menu.game_mode', return_value=2)
    def test_game_mode_2(self, mock_game_mode, mock_print_menu):
        with patch('game.Game.game_loop') as mock_game_loop:
            main()
            mock_print_menu.assert_called_once()
            mock_game_mode.assert_called_once_with()
            mock_game_loop.assert_called_once()

    @patch('menu.Menu.print_menu', return_value=True)
    @patch('menu.Menu.game_mode', return_value=1)
    def test_game_mode_1(self, mock_game_mode, mock_print_menu):
        with patch('ai.Ai.game_loop') as mock_ai_game_loop:
            main()
            mock_print_menu.assert_called_once()
            mock_game_mode.assert_called_once_with()
            mock_ai_game_loop.assert_called_once()
