class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        pm = A[0] + 0  # past max of A[i] + i
        out = float("-inf")
        for j in range(1, len(A)):
            # add the max of A[i] + i and the current A[j] - j
            out = max(out, A[j] - j + pm)
            pm = max(pm, A[j] + j)
        return out
