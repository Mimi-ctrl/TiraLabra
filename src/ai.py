import numpy
from game import Game


class Ai:
    def __init__(self):
        self.board = numpy.zeros((6, 7))
        self.player = 1
        self.game = Game()

    def game_loop(self):
        """Print game board and ask column for player 1. Call drop piece for adding piece to
        board. Call check win for checking if there any win. Change player if no win. 
        When it's player 2's turn, it call find best move to find best move for AI."""
        print("\nChoose column 0-6, Player 1 start.\n")
        print(self.board)
        while True:
            if self.game.check_is_board_full(self.board):
                print("Draw match")
                break
            if self.player == 1:
                column = input("Choose column: ")
                if column.isnumeric():
                    column = int(column)
                    if self.game.drop_piece(self.board, column, self.player):
                        self.player = 2
                else:
                    print("Invalid column.")
                    continue
            elif self.player == 2:
                ai_move = self.find_best_move(self.board)
                self.game.drop_piece(self.board, ai_move, self.player)
                self.player = 1
            print(self.board)
            if self.game.check_win(self.board):
                break

    def find_best_move(self, board):
        """Find the best move for the AI to make, considering the current state of the board."""
        best_move = -1
        best_score = -10**9
        col = 3
        minus_plus = 0
        calc = True
        for number in range(7):
            temp_board = board.copy()
            if calc:
                self.make_move(temp_board, col - minus_plus, 2)
                score = self.minimax(temp_board, 4, -10**9, 10**9, False)
                if score > best_score:
                    best_score = score
                    best_move = col - minus_plus
                calc = False
            else:
                self.make_move(temp_board, col + minus_plus, 2)
                score = self.minimax(temp_board, 4, -10**9, 10**9, False)
                if score > best_score:
                    best_score = score
                    best_move = col + minus_plus
                calc = True
            if number % 2 == 0:
                minus_plus += 1
        return best_move

    def make_move(self, board, col, player):
        """Make a move on the game board for the specified player by placing their piece in the chosen column."""
        for row in reversed(range(6)):
            if board[row][col] == 0:
                board[row][col] = player
                break

    def minimax(self, board, depth, alpha, beta, ai_turn):
        """Perform the minimax algorithm to evaluate and determine the best move for the AI."""
        if (depth == 0 or self.game.check_is_board_full(board)
                or self.is_winning_move(board, 1) or self.is_winning_move(board, 2)):
            return self.evaluate_position(board, 2) - self.evaluate_position(board, 1)
        if ai_turn:
            max_eval = -10**9
            for col in range(7):
                temp_board = board.copy()
                self.make_move(temp_board, col, 2)
                evaluation = self.minimax(
                    temp_board, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, evaluation)
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            return max_eval
        min_eval = 10**9
        for col in range(7):
            temp_board = board.copy()
            self.make_move(temp_board, col, 1)
            evaluation = self.minimax(
                temp_board, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return min_eval

    def is_winning_move(self, board, player):
        """Check if the player has a winning move on the current game board."""
        for row in board:
            for column in range(len(row)-3):
                if row[column] == player:
                    if row[column] == row[column+1] == row[column+2] == row[column+3]:
                        return True
        for row in range(len(board)-3):
            for column in range(len(board[row])):
                if board[row][column] == player:
                    if (board[row][column] == board[row+1][column] ==
                            board[row+2][column] == board[row+3][column]):
                        return True
        for row in range(0, len(board)-3):
            for column in range(0, len(board[row])-3):
                if board[row][column] == player:
                    if (board[row][column] == board[row+1][column+1] ==
                            board[row+2][column+2] == board[row+3][column+3]):
                        return True
        for row in range(len(board)-3):
            for column in range(3, len(board[row])):
                if board[row][column] == player:
                    if (board[row][column] == board[row+1][column-1] ==
                            board[row+2][column-2] == board[row+3][column-3]):
                        return True
        return False

    def evaluate_position(self, board, player):
        """Evaluate the current position on the game board for the specified player."""
        score = 0
        for row in range(6):
            for col in range(7 - 3):
                line = [board[row][col+i] for i in range(4)]
                score += self.evaluate_line(line, player)
        for col in range(7):
            for row in range(6 - 3):
                line = [board[row+i][col] for i in range(4)]
                score += self.evaluate_line(line, player)
        for row in range(6 - 3):
            for col in range(7 - 3):
                line = [board[row+i][col+i] for i in range(4)]
                score += self.evaluate_line(line, player)
                line = [board[row+3-i][col+i] for i in range(4)]
                score += self.evaluate_line(line, player)
        return score

    def evaluate_line(self, line, player):
        """Evaluate a line of game pieces for its strategic importance to the specified player."""
        score = 0
        opponent_player = 1 if player == 2 else 2
        if line.count(player) == 4:
            score += 100
        elif line.count(player) == 3 and line.count(0) == 1:
            score += 5
        elif line.count(player) == 2 and line.count(0) == 2:
            score += 2
        if line.count(opponent_player) == 3 and line.count(0) == 1:
            score -= 4
        return score
