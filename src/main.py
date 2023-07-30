from ai import Ai
from game import Game


def main():
    selection = Game.print_menu()
    if selection == True:
        mode = Game.game_mode()
        if mode == 2:
            Game.game_loop()
        # if mode == 1:


if __name__ == "__main__":
    main()
