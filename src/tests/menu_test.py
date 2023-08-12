import unittest
from unittest.mock import patch
from menu import Menu


class TestMenu(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_print_menu_new_game(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = Menu.print_menu()
            mock_print.assert_called()
            self.assertTrue(result)

    @patch('builtins.input', side_effect=['2'])
    def test_print_menu_exit(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = Menu.print_menu()
            mock_print.assert_called()
            self.assertFalse(result)

    @patch('builtins.input', side_effect=['3', '1'])
    def test_print_menu_invalid_then_new_game(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = Menu.print_menu()
            mock_print.assert_called()
            self.assertTrue(result)

    @patch('builtins.input', side_effect=['a', '2'])
    def test_print_menu_nonnumeric_then_exit(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = Menu.print_menu()
            mock_print.assert_called()
            self.assertFalse(result)

    @patch('builtins.input', side_effect=['1'])
    def test_game_mode_computer(self, mock_input):
        result = Menu.game_mode()
        self.assertEqual(result, 1)

    @patch('builtins.input', side_effect=['2'])
    def test_game_mode_player_2(self, mock_input):
        result = Menu.game_mode()
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=['3', '1'])
    def test_game_mode_invalid_then_computer(self, mock_input):
        result = Menu.game_mode()
        self.assertEqual(result, 1)

    @patch('builtins.input', side_effect=['a', '2'])
    def test_game_mode_nonnumeric_then_player_2(self, mock_input):
        result = Menu.game_mode()
        self.assertEqual(result, 2)
