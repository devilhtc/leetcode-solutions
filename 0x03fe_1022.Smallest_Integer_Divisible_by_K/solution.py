class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        # idea: keep dividing
        # if something still remains, add a 1 at the end
        l = 1
        rem = 1
        while rem > 0 and l <= K:
            # not enough -> add 1 at the end
            # keep track of length
            if rem < K:
                rem = rem * 10 + 1
                l += 1
                continue
            # enough -> divide and take remainder
            rem = rem % K
            if rem == 0:
                return l
        return -1
