class Menu:

    @staticmethod
    def print_menu():
        """Print menu where user can choose new game or exit."""
        print("🄲 🄾 🄽 🄽 🄴 🄲 🅃  🄵 🄾 🅄 🅁")
        print(
            "\n--------------------------\n1: New Game\n2: Exit\n--------------------------")
        while True:
            answer = input("\n--> ")
            if answer.isnumeric():
                answer = int(answer)
                if answer == 1:
                    return True
                if answer == 2:
                    print("\nBye!")
                    return False
                print("\nInvalid input!")
                continue
            print("\nInvalid input!")
            continue

    @staticmethod
    def game_mode():
        """Print menu where user can choose which mode."""
        print("\n--------------------------\n1: Computer\n2: Player 2\n--------------------------")
        while True:
            answer = input("\n--> ")
            if answer.isnumeric():
                answer = int(answer)
                if answer == 1:
                    return 1
                if answer == 2:
                    return 2
                print("\nInvalid input!")
                continue
            print("\nInvalid input!")
            continue
