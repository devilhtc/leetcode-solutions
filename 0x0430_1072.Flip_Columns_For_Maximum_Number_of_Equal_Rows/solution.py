class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def row2key(row):
            if row[0] == 0:
                return "".join(map(str, row))
            return "".join(map(lambda i: str(1 - i), row))

        d = collections.defaultdict(int)
        for row in matrix:
            d[row2key(row)] += 1
        return max(d.values())


class Solution2:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        return max(
            collections.Counter(
                map(
                    lambda row: "".join(
                        map(str, [e if row[0] else (1 - e) for e in row])
                    ),
                    matrix,
                )
            ).values()
        )
