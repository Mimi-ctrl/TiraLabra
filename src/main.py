from ai import Ai
from game import Game


def main():
    game = Game()
    ai = Ai()
    selection = game.print_menu()
    if selection:
        mode = game.game_mode()
        if mode == 2:
            game.game_loop()
        if mode == 1:
            ai.game_loop_with_ai()


if __name__ == "__main__":
    main()
