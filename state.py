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

    def whether_is_goal(self):
        goal=[[1,2,3], [4,5,6], [7,8,0]]
        return self.board == goal
    #determine whether the current state is goal


    def try_moves(self ):
        #try possible move
        i,j = self.blank
        moves =[]

        if(i>0): moves.append('up')
        if(j>0): moves.append('left')
        if(i<len(self.board)-1): moves.append('down')
        if(j<len(self.board[0])-1): moves.append('right')

        return moves

    def move(self, direction):
        #make a move and change to a new state
        i, j = self.blank
        new_board = copy.deepcopy(self.board)

        if direction == 'up':
            new_board[i][j], new_board[i - 1][j] = new_board[i - 1][j], new_board[i][j]
        elif direction == 'down':
            new_board[i][j], new_board[i + 1][j] = new_board[i + 1][j], new_board[i][j]
        elif direction == 'left':
            new_board[i][j], new_board[i][j - 1] = new_board[i][j - 1], new_board[i][j]
        elif direction == 'right':
            new_board[i][j], new_board[i][j + 1] = new_board[i][j + 1], new_board[i][j]

        return PuzzleState(new_board, self, direction, self.cost + 1)

    def misplaced_tile(self):
        #misplaced tile heuristic function
        count = 0
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] != 0 and self.board[i][j] != goal[i][j]:
                    count += 1

        return count

    def manhattan_distance(self):
        #manhattan distance heuristic
        distance = 0

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                tile = self.board[i][j]
                if tile != 0:
                    # 计算tile的目标位置
                    goal_i, goal_j = (tile - 1) // 3, (tile - 1) % 3
                    distance += abs(i - goal_i) + abs(j - goal_j)

        return distance


    def print_board(self):
        #print the board
        for row in self.board:
            print(" ".join(str(x) if x != 0 else "_" for x in row))
        print()


