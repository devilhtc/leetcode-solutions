class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        rem = A[0]
        out = [A[0] == 0]
        for i in range(1, len(A)):
            rem = (rem * 2 + A[i]) % 5
            out.append(rem == 0)
        return out
