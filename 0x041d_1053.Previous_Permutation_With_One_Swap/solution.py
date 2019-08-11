class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        stack = []
        l = len(A)
        swap = (-1, -1, 0)

        for k in range(l):
            i = l - 1 - k
            while len(stack) > 0 and stack[-1][1] < A[i]:
                j, x = stack.pop()
                d = A[i] - x
                curswap = (i, j, d)
                if swap[0] != i:
                    swap = curswap if i > swap[0] else swap
                elif d != swap[1]:
                    swap = curswap if d < swap[2] else swap
                else:
                    swap = curswap if j < swap[1] else swap
            stack.append((i, A[i]))

        if swap == (-1, -1, 0):
            return A
        i, j = swap[:2]
        A[i], A[j] = A[j], A[i]
        return A
