class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def validate_vals(vals):
            return all(
                v == 1
                for _, v in collections.Counter(
                    [int(v) for v in vals if v != "."]
                ).items()
            )

        def validate_row(i):
            return validate_vals(board[i])

        def validate_col(i):
            return validate_vals([board[j][i] for j in range(9)])

        def validate_box(i, j):
            return validate_vals(
                [
                    board[m][n]
                    for m in range(i * 3, i * 3 + 3)
                    for n in range(j * 3, j * 3 + 3)
                ]
            )

        return (
            all(validate_row(i) for i in range(9))
            and all(validate_col(i) for i in range(9))
            and all(validate_box(i, j) for i in range(3) for j in range(3))
        )
