class Solution:
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        num1s = sum(A)
        if num1s % 3 != 0:  # impossible
            return [-1, -1]
        if all(ele == 0 for ele in A):  # all 0s, return any
            return [0, 2]

        p = num1s // 3  # periods
        ss = []  # starting indices
        es = []  # ending indices
        c = 0

        for i, v in enumerate(A):
            if v == 1:
                c += 1
                if (c - 1) % p == 0:
                    ss.append(i)
                if c % p == 0:
                    es.append(i)

        zs = [  # number of 0s between each run (and at the start and end)
            ss[0],
            ss[1] - es[0] - 1,
            ss[2] - es[1] - 1,
            len(A) - es[2] - 1,
        ]
        if not (
            (es[0] - ss[0])
            == (es[1] - ss[1])
            == (es[2] - ss[2])  # runs must have the length
            and all(
                A[ss[0] + i] == A[ss[1] + i] == A[ss[2] + i]
                for i in range(1, es[0] - ss[0])
            )  # same binary rep
            and zs[1]
            >= zs[3]
            <= zs[2]  # seperable (since the last number takes all the trailing 0s)
        ):
            return [-1, -1]
        return [es[0] + zs[3], es[1] + zs[3] + 1]
