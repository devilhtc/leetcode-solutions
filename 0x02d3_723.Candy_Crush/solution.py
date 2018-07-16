class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        self.m = len(board)
        self.n = len(board[0])
        b = board
        newboard = self.iterate(board)
        while not self.areSame(board, newboard):
            board = newboard
            newboard = self.iterate(board)
        return newboard

    def crush(self, board):
        newboard = self.createNewBoard(0)
        status = self.createNewBoard(1)
        for i in range(self.m):
            for j in range(self.n):
                self.flip(board, status, i, j)

        for i in range(self.m):
            for j in range(self.n):
                newboard[i][j] = status[i][j] * board[i][j]
        return newboard

    def flip(self, board, status, i, j):
        # returns 0 if it can be removed
        cur = board[i][j]
        if cur == 0:
            return  # its already 0
        if i < self.m - 2:
            if board[i + 2][j] == board[i + 1][j] and board[i + 1][j] == cur:
                status[i + 2][j] = 0
                status[i + 1][j] = 0
                status[i][j] = 0
        if j < self.n - 2:
            if board[i][j + 2] == board[i][j + 1] and board[i][j + 1] == cur:
                status[i][j + 2] = 0
                status[i][j + 1] = 0
                status[i][j] = 0

    def createNewBoard(self, val):
        return [[val for _ in range(self.n)] for xxx in range(self.m)]

    def drop(self, board):
        newboard = self.createNewBoard(0)
        for j in range(self.n):
            k = self.m - 1
            for i in range(self.m - 1, -1, -1):
                if board[i][j] > 0:
                    newboard[k][j] = board[i][j]
                    k -= 1
        return newboard

    def iterate(self, board):
        return self.drop(self.crush(board))

    def areSame(self, board1, board2):

        for i in range(self.m):
            for j in range(self.n):
                if board1[i][j] != board2[i][j]:
                    return False
        return True
