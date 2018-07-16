# solution by @lee215 distilled to its essence lol


class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)
        if any(
            board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]
            for i in range(N)
            for j in range(N)
        ):
            return -1
        rowSum, colSum = sum(board[0]), sum(board[i][0] for i in range(N))
        if (
            rowSum < N / 2
            or rowSum > (N + 1) / 2
            or colSum < N / 2
            or colSum > (N + 1) / 2
        ):
            return -1
        rowSwap, colSwap = (
            sum(board[i][0] == i % 2 for i in range(N)),
            sum(board[0][i] == i % 2 for i in range(N)),
        )
        transform2 = lambda x: [min(N - x, x), [x, N - x][x % 2]][N % 2]
        rowSwap = transform2(rowSwap)
        colSwap = transform2(colSwap)
        return (rowSwap + colSwap) / 2
