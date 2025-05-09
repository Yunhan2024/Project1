import copy

class PuzzleState:
    def __init__(self, board, parent=None, action= None, cost=0):
        self.board = board
        self.parent = parent
        self.action = action
        self.cost = cost
        #initialize the state

        for i in range(len(board)): # try to be extensive
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    self.blank = (i, j)
                    return
    # find where is space