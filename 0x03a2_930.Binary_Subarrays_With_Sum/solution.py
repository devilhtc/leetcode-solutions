class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        if S == 0:
            rl = 0
            out = 0
            for v in A:
                if v == 0:
                    rl += 1
                else:
                    out += (rl + 1) * rl // 2
                    rl = 0
            out += (rl + 1) * rl // 2
            return out
        ones = [i for i, v in enumerate(A) if v == 1]
        i = 0
        j = S - 1
        out = 0
        while j < len(ones):
            l = (ones[0] + 1) if i == 0 else (ones[i] - ones[i - 1])
            r = (len(A) - ones[-1]) if j == len(ones) - 1 else (ones[j + 1] - ones[j])
            out += l * r
            i += 1
            j += 1
        return out
