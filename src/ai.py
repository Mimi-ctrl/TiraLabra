from game import Game


class Ai:
    def __init__(self):
        self.game = Game()
        self.board = self.game.board

    def game_loop_with_ai(self):
        """???"""
        player = 1
        print("\nYou are Player 1 and ai is Player 2. Choose column 0-6, Player 1 start.\n")
        while True:
            print(self.board)
            if player == 1:
                column = input("Choose column: ")
                if column.isnumeric():
                    column = int(column)
                    self.game.drop_piece(column, player)
                    player = 2
                    if self.game.check_win():
                        break
                else:
                    print("Invalid column.")
                    continue
            elif player == 2:
                ai_move = self.minimax(self.board)
                self.game.drop_piece(ai_move, player)
                player = 1
                if self.game.check_win():
                    break

    def minimax(self, board):
        best_move = None
        best_eval = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        depth = 5
        for move in self.mahdolliset_siirrot(board):
            new_board = self.tee_siirto(board, move, 2)
            eval = self.alphabeta(new_board, depth, alpha, beta, False)
            if eval.any() > best_eval:
                best_eval = eval
                best_move = move
            alpha = max(alpha, best_eval)
        return best_move

    def tee_siirto(self, board, col, player):
        for row in range(5, -1, -1):
            if board[row][col] == 0:
                board[row][col] = player
                return board
        return None

    def mahdolliset_siirrot(self, board):
        mahdolliset = []
        for col in range(7):
            if self.laita_siirto(board, col, 2):
                mahdolliset.append(col)
                self.laita_siirto(board, col, 0)
        return mahdolliset

    def laita_siirto(self, board, col, player):
        print(board)
        print(col)
        print(player)
        for row in range(5, -1, -1):
            if board[row][col] == 0:
                board[row][col] = player
                return True
        return False

    def alphabeta(self, board, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or self.peli_on_paattynyt(board):
            return board

        if maximizingPlayer:
            maxEval = float('-inf')
            for move in self.mahdolliset_siirrot(board):
                new_board = self.tee_siirto(board, move, 2)
                eval = self.alphabeta(new_board, depth - 1, alpha, beta, False)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, maxEval)
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = float('inf')
            for move in self.mahdolliset_siirrot(board):
                new_board = self.tee_siirto(board, move, 0)
                eval = self.alphabeta(new_board, depth - 1, alpha, beta, True)
                minEval = min(minEval, eval)
                beta = min(beta, minEval)
                if beta <= alpha:
                    break
            return minEval

    def peli_on_paattynyt(self, board):
        if self.check_win(board):
            return True
        for row in range(6):
            for col in range(7):
                if board[row][col] == 0:
                    return False
        return True

    def check_win(self, board):
        for row in board:
            for column in range(len(row)-3):
                if row[column] == 1 or row[column] == 2:
                    if row[column] == row[column+1] == row[column+2] == row[column+3]:
                        return True
        for row in range(len(board)-3):
            for column in range(len(board[row])):
                if board[row][column] == 1 or board[row][column] == 2:
                    if (board[row][column] == board[row+1][column] ==
                            board[row+2][column] == board[row+3][column]):
                        return True
        for row in range(0, len(board)-3):
            for column in range(0, len(board[row])-3):
                if board[row][column] == 1 or board[row][column] == 2:
                    if (board[row][column] == board[row+1][column+1] ==
                            board[row+2][column+2] == board[row+3][column+3]):
                        return True
        for row in range(len(board)-3):
            for column in range(3, len(board[row])):
                if board[row][column] == 1 or board[row][column] == 2:
                    if (board[row][column] == board[row+1][column-1] ==
                            board[row+2][column-2] == board[row+3][column-3]):
                        return True
        return None
