#from ai import Ai
from game import Game


def main():
    game = Game()
    selection = game.print_menu()
    if selection:
        mode = game.game_mode()
        if mode == 2:
            game.game_loop()
        # if mode == 1:


if __name__ == "__main__":
    main()
