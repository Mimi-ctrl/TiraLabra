import numpy


class Game:

    def __init__(self, board=numpy.zeros((6, 7))):
        self.board = board
        self.game = Game

    @staticmethod
    def print_menu():
        """Print menu where user can choose new game or exit."""
        print("🄲 🄾 🄽 🄽 🄴 🄲 🅃  🄵 🄾 🅄 🅁")
        print(
            "\n--------------------------\n1: New Game\n2: Exit\n--------------------------")
        while True:
            answer = int(input("\n--> "))
            if answer == 1:
                return True
            if answer == 2:
                print("\nBye!")
                return False
            print("\nInvalid input!")
            continue

    @staticmethod
    def game_mode():
        """Print menu where user can choose which mode."""
        print("\n--------------------------\n1: Computer\n2: Player 2\n--------------------------")
        while True:
            answer = int(input("\n--> "))
            if answer == 1:
                return 1
            if answer == 2:
                return 2
            print("\nInvalid input!")
            continue

    def game_loop(self):
        """Print game board and ask column. Call drop piece for adding piece to
        board. Call check win for checking if there any win. Change player if no win."""
        player = 1
        print("\nChoose column 0-6, Player 1 start.\n")
        print(self.board)
        while True:
            column = int(input("Choose column: "))
            self.game().drop_piece(column, player)
            print(self.board)
            if self.game().check_win():
                break
            if player == 1:
                player = 2
            else:
                player = 1

    def is_valid_column(self, column):
        """Check if given column valid."""
        if 0 <= column <= 6:
            if int(self.board[0][column]) == 0:
                return True
        else:
            return False
        return None

    def drop_piece(self, column, player):
        """Drop piece to column if valid. Call is valid column to make sure is valid."""
        if self.game().is_valid_column(column):
            for row in range(len(self.board)-1, -1, -1):
                if self.board[row][column] == 0:
                    self.board[row][column] = player
                    return True
        else:
            print("Column full or invalid column. Please try another column.")
            return False
        return None

    def check_win(self):
        """Check horizontal, vertical, positive diagonal and negative diagonal if 4.
        Return true if win."""
        for row in self.board:
            for column in range(len(row)-3):
                if row[column] == 1 or row[column] == 2:
                    if row[column] == row[column+1] == row[column+2] == row[column+3]:
                        print("Player ", str(row[column])[0], "wins!")
                        return True
        for row in range(len(self.board)-3):
            for column in range(len(self.board[row])):
                if self.board[row][column] == 1 or self.board[row][column] == 2:
                    if (self.board[row][column] == self.board[row+1][column] ==
                            self.board[row+2][column] == self.board[row+3][column]):
                        print("Player ", str(
                            self.board[row][column])[0], "wins!")
                        return True
        for row in range(0, len(self.board)-3):
            for column in range(0, len(self.board[row])-3):
                if self.board[row][column] == 1 or self.board[row][column] == 2:
                    if (self.board[row][column] == self.board[row+1][column+1] ==
                            self.board[row+2][column+2] == self.board[row+3][column+3]):
                        print("Player ", str(
                            self.board[row][column])[0], "wins!")
                        return True
        for row in range(len(self.board)-3):
            for column in range(3, len(self.board[row])):
                if self.board[row][column] == 1 or self.board[row][column] == 2:
                    if (self.board[row][column] == self.board[row+1][column-1] ==
                            self.board[row+2][column-2] == self.board[row+3][column-3]):
                        print("Player ", str(
                            self.board[row][column])[0], "wins!")
                        return True
        return None
