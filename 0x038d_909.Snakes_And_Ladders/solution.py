class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)
        
        jumps = {}
        for i in range(N):
            for j in range(N):
                n = (N - i - 1) * N + ((j + 1) if (N - i - 1) % 2 == 0 else (N - j))
                if board[i][j] != -1:
                    jumps[n] = board[i][j]
        
        board_step = [N * N + 1] * (N * N)
        board_step[0] = 0
        queue = [0]
        c = 0
        
        while c < len(queue):
            i = queue[c]
            c = c + 1
            n = i + 1
            def step(x):
                if board_step[x] > board_step[i] + 1:
                    board_step[x] = board_step[i] + 1
                    queue.append(x)
                
            for j in range(i + 1, i + 7):
                if j >= N * N:
                    continue
                if j + 1 in jumps:
                    k = jumps[j + 1] - 1
                    step(k)
                else:
                    step(j)

        return -1 if board_step[-1] == N * N + 1 else board_step[-1]