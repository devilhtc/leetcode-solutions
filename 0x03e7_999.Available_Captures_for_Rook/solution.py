class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def fr():
            for i in range(8):
                for j in range(8):
                    if board[i][j] == "R":
                        return i, j

        def fp(li, lj):
            if isinstance(li, int):
                li = [li] * len(lj)
            else:
                lj = [lj] * len(li)
            for i, j in zip(li, lj):
                if board[i][j] == "p":
                    return 1
                elif board[i][j] != ".":
                    return 0
            return 0

        def rangel(i, j):
            return list(range(i, j, 1 if i < j else -1))

        ri, rj = fr()
        out = 0

        return (
            fp(rangel(ri + 1, 8), rj)
            + fp(rangel(ri - 1, -1), rj)
            + fp(ri, rangel(rj + 1, 8))
            + fp(ri, rangel(rj - 1, -1))
        )
