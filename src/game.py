import numpy


class Game:

    def print_menu():
        """ Print menu where user can choose new game or exit.
        """
        print("🄲 🄾 🄽 🄽 🄴 🄲 🅃  🄵 🄾 🅄 🅁")
        print("\n---------------------------\n1: New Game\n2: Exit\n---------------------------")
        while True:
            answer = int(input("\n--> "))
            if answer == 1:
                return True
            if answer == 2:
                print("\nBye!")
                return False
            else:
                print("\nInvalid input!")
                continue

    def game_mode():
        """Print menu where user can choose which mode.
        """
        print("\n---------------------------\n1: Computer\n2: Player 2\n---------------------------")
        while True:
            answer = int(input("\n--> "))
            if answer == 1:
                return 1
            if answer == 2:
                return 2
            else:
                print("\nInvalid input!")
                continue   

    def game_loop():
        """Print game board and ask column.
        """
        board = Game.create_board()
        player = 1
        print("\nChoose column 0-6, Player 1 start.\n")
        print(board)
        while True:
            column = int(input("Choose column: "))
            Game.drop_piece(board, column, player)
            print(board)
            if Game.check_win(board):
                break
            else:
                if player == 1:
                    player = 2
                else:
                    player = 1

    def create_board():
        """Create 6x7 game board filled with 0.
        """
        ROWS = 6
        COLUMNS = 7
        board = numpy.zeros((ROWS, COLUMNS))
        return board

    def is_valid_column(board, col):
        """Check if given column valid.
        """
        if col <= 6 and col >= 0:
            if int(board[0][col]) == 0:
                return True
        else:
            return False

    def drop_piece(board, col, player):
        """Drop piece to column if valid.  
        """
        if Game.is_valid_column(board, col):
            for r in range(len(board)-1, -1, -1):
                if board[r][col] == 0:
                    board[r][col] = player
                    return True
        else:
            print("Column full or invalid column. Please try another column.")
            return False

    def check_win(board):
        """Check horizontal, vertical, positive diagonal and negative diagonal if 4.
        """
        for x in board:
            for y in range(len(x)-3):
                if x[y] == 1 or x[y] == 2:
                    if x[y] == x[y+1] == x[y+2] == x[y+3]:
                        print("Player ", str(x[y])[0],"wins!")
                        return True                 
        for x in range(len(board)-3):
            for y in range(len(board[x])):
                if board[x][y] == 1 or board[x][y] == 2:
                    if board[x][y] == board[x+1][y] == board[x+2][y] == board[x+3][y]:
                        print("Player ", str(board[x][y])[0],"wins!")
                        return True
        for x in range(0,len(board)-3):
            for y in range(0,len(board[x])-3):
                if board[x][y] == 1 or board[x][y] == 2:
                    if board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3]:
                        print("Player ", str(board[x][y])[0],"wins!")
                        return True
        for x in range(len(board)-3):  
            for y in range(3, len(board[x])):
                if board[x][y] == 1 or board[x][y] == 2:
                    if board[x][y] == board[x+1][y-1] == board[x+2][y-2] == board[x+3][y-3]:
                        print("Player ", str(board[x][y])[0],"wins!")
                        return True