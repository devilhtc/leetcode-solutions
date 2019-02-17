"""
naive TLE solution:

class Solution:
    def minKBitFlips(self, A: 'List[int]', K: 'int') -> 'int':
        out = 0
        l = len(A)
        for i in range(l):
            if A[i] == 0:
                if i > l - K:
                    return -1
                for j in range(i, i + K):
                    A[j] = 1 - A[j]
                out += 1
        return out
"""


class Solution:
    def minKBitFlips(self, A: "List[int]", K: "int") -> "int":
        out = 0  # total number of flips
        l = len(A)
        flipq = collections.deque([])  # queue of flip end points
        flips = 0  # current number of flips

        for i in range(l):
            A[i] = (A[i] + flips) % 2
            if A[i] == 0:
                if i > l - K:  # cant flip beyond l - K
                    return -1
                # else flip the current element
                # keep track of end point
                A[i] = 1
                flips += 1
                out += 1
                flipq.append(i + K - 1)

            # if the current index is an end point, pop it
            if len(flipq) > 0 and flipq[0] == i:
                flipq.popleft()
                flips -= 1

        return out
