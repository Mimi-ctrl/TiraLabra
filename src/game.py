import numpy

class Game:
    def __init__(self):
        return

    def create_board():
        """Create 6x7 board
        """
        ROWS = 6
        COLUMNS = 7
        board = numpy.zeros((ROWS, COLUMNS))
        return board
    
    def is_valid_column(board,col):  
        """Check is
        """
        if int(board[0][col]) == 0:    
            return True  
        else:    return False
        
    def drop_piece(board,col,player): 
        if is_valid_column(board,col):  
            for r in range(len(board)-1,-1,-1):   
                if board[r][col] == 0: 
                    board[r][col] = player       
                    return True   
        else:    
            print("Column full. Please try another column.")    
            return False
        