import numpy


class Game:

    def __init__(self):
        self.board = numpy.zeros((6, 7))

    def game_loop(self):
        """Print game board and ask column. Call drop piece for adding piece to
        board. Call check win for checking if there any win. Change player if no win."""
        player = 1
        print("\nChoose column 0-6, Player 1 start.\n")
        print(self.board)
        while True:
            if self.check_is_board_full(self.board):
                print("Draw match")
                break
            column = input("Choose column: ")
            if column.isnumeric():
                column = int(column)
                if self.drop_piece(self.board, column, player):
                    if player == 1:
                        player = 2
                    else:
                        player = 1
                print(self.board)
                if self.check_win(self.board):
                    break
            else:
                print("Invalid column.")
                print(self.board)
                continue

    def is_valid_column(self, board, column):
        """Check if given column valid."""
        if 0 <= column <= 6:
            if int(board[0][column]) == 0:
                return True
        else:
            return False
        return None

    def drop_piece(self, board, column, player):
        """Drop piece to column if valid. Call is valid column to make sure is valid."""
        if self.is_valid_column(board, column):
            for row in range(len(board)-1, -1, -1):
                if board[row][column] == 0:
                    board[row][column] = player
                    return True
        else:
            print("Column full or invalid column. Please try another column.")
            return False
        return None

    def check_is_board_full(self, board):
        """Check board is it full. If board is full return True."""
        for row in board:
            for cell in row:
                if cell == 0:
                    return False
        return True

    def check_win(self, board):
        """Check horizontal, vertical, positive diagonal and negative diagonal if 4.
        Return true if win."""
        for row in board:
            for column in range(len(row)-3):
                if row[column] == 1 or row[column] == 2:
                    if row[column] == row[column+1] == row[column+2] == row[column+3]:
                        print("Player ", str(row[column])[0], "wins!")
                        return True
        for row in range(len(board)-3):
            for column in range(len(board[row])):
                if board[row][column] == 1 or board[row][column] == 2:
                    if (board[row][column] == board[row+1][column] ==
                            board[row+2][column] == board[row+3][column]):
                        print("Player ", str(
                            board[row][column])[0], "wins!")
                        return True
        for row in range(0, len(board)-3):
            for column in range(0, len(board[row])-3):
                if board[row][column] == 1 or board[row][column] == 2:
                    if (board[row][column] == board[row+1][column+1] ==
                            board[row+2][column+2] == board[row+3][column+3]):
                        print("Player ", str(
                            board[row][column])[0], "wins!")
                        return True
        for row in range(len(board)-3):
            for column in range(3, len(board[row])):
                if board[row][column] == 1 or board[row][column] == 2:
                    if (board[row][column] == board[row+1][column-1] ==
                            board[row+2][column-2] == board[row+3][column-3]):
                        print("Player ", str(
                            board[row][column])[0], "wins!")
                        return True
        return None
