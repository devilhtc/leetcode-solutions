class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # quick select with group of 5
        g = 5

        def mom(arr):
            # medium of mediu
            ms = []
            i = 0
            while i < len(arr):
                sub_arr = arr[i : min(len(arr), i + g)]
                ms.append(sorted(sub_arr)[len(sub_arr) // 2])
                i += g
            out = dac(ms, len(ms) // 2)
            return out

        def dac(arr, o):
            # divide and conquer
            if o == 1:
                return max(arr)
            elif o == len(arr):
                return min(arr)

            if len(arr) < 10:
                return sorted(arr)[-o]

            p = mom(arr)
            l, m, h = [], [], []
            for a in arr:
                if a < p:
                    l.append(a)
                elif a == p:
                    m.append(p)
                else:
                    h.append(a)

            if o <= len(h):
                return dac(h, o)
            elif len(h) + len(m) >= o > len(h):
                return p
            else:
                return dac(l, o - len(h) - len(m))

        return dac(nums, k)

    def minMoves2(self, nums: List[int]) -> int:
        m = self.findKthLargest(nums, (len(nums) + 1) // 2)
        return sum(abs(ele - m) for ele in nums)
