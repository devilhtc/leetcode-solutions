class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if all(ele < 0 for ele in A):
            return max(A)
        if all(ele >= 0 for ele in A):
            return sum(A)

        s = sum(A)
        accu = [0]
        for ele in A:
            accu.append(accu[-1] + ele)

        out = 0
        i = j = 0  # min index, max index
        for k, v in enumerate(accu):
            out = max(max(v - accu[i], s - (v - accu[j])), out)
            if v <= accu[i]:
                i = k
            if v >= accu[j]:
                j = k
        return out
