import numpy
from game import Game


class Ai:
    def __init__(self):
        self.board = numpy.zeros((6, 7))
        self.player = 1
        self.game = Game()

    def game_loop(self):
        """????"""
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
        """???"""
        best_move = -1
        best_score = float('-inf')
        for col in range(7):
            if self.is_valid_move(board, col):
                temp_board = board.copy()
                self.make_move(temp_board, col, 2)
                score = self.minimax(temp_board, 4, float(
                    '-inf'), float('inf'), False)
                if score > best_score:
                    best_score = score
                    best_move = col
        return best_move

    def is_valid_move(self, board, col):
        """????"""
        return board[6 - 1][col] == 0

    def make_move(self, board, col, player):
        """???"""
        for row in range(6):
            if board[row][col] == 0:
                board[row][col] = player
                break

    def minimax(self, board, depth, alpha, beta, ai_turn):
        """???"""
        if (depth == 0 or self.game.check_is_board_full(board)
                or self.is_winning_move(board, 1) or self.is_winning_move(board, 2)):
            return self.evaluate_position(board, 2) - self.evaluate_position(board, 1)
        if ai_turn:
            max_eval = float('-inf')
            for col in range(7):
                if self.is_valid_move(board, col):
                    temp_board = board.copy()
                    self.make_move(temp_board, col, 2)
                    evaluation = self.minimax(
                        temp_board, depth - 1, alpha, beta, False)
                    max_eval = max(max_eval, evaluation)
                    alpha = max(alpha, evaluation)
                    if beta <= alpha:
                        break
            return max_eval
        min_eval = float('inf')
        for col in range(7):
            if self.is_valid_move(board, col):
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
        """???"""
        for row in range(6):
            for col in range(7 - 3):
                if all(board[row][col+i] == player for i in range(4)):
                    return True
        for col in range(7):
            for row in range(6 - 3):
                if all(board[row+i][col] == player for i in range(4)):
                    return True
        for row in range(6 - 3):
            for col in range(7 - 3):
                if all(board[row+i][col+i] == player for i in range(4)):
                    return True
                if all(board[row+3-i][col+i] == player for i in range(4)):
                    return True
        return False

    def evaluate_position(self, board, player):
        """???"""
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
        """???"""
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
