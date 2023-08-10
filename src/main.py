from ai import Ai
from game import Game
from menu import Menu


def main():
    game = Game()
    ai_game = Ai()
    menu = Menu()
    selection = menu.print_menu()
    if selection:
        mode = menu.game_mode()
        if mode == 2:
            game.game_loop()
        if mode == 1:
            ai_game.game_loop()


if __name__ == "__main__":
    main()
