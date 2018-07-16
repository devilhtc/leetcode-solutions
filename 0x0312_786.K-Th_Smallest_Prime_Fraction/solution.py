# note: this implementation uses list to represent fraction number
# which might be inefficient
# a better way would be using a struct in C


class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """

        def minus(a, b):
            return [a[0] * b[1] - a[1] * b[0], a[1] * b[1]]

        def get_max(nums):
            m = [nums[0], nums[1]]
            for i in range(1, len(nums) - 1):
                cur = [nums[i], nums[i + 1]]
                if minus(cur, m)[0] > 0:
                    m = cur
            return m

        def ave(a, b):
            return [a[0] * b[1] + a[1] * b[0], a[1] * b[1] * 2]

        A = sorted(A)
        l = len(A)
        lo_all = [A[0], A[-1]]
        hi_all = get_max(A)

        # return two closest fraction numbers (in the array) in the form of [p, q, k]
        # one less than or equal to val, one greater than or equal to val
        # basically traversing a 2d grid with elements ordered in rows and columns
        # suppose elements are ordered in ascending order in rows and columns
        # we need only to step up and right
        def search(nums, val):
            cur_lo = lo_all
            lo_gap = minus(val, cur_lo)
            cur_hi = hi_all
            hi_gap = minus(cur_hi, val)
            i = 0
            j = 1
            cover = 0
            while i < l - 1:
                if j == l:
                    break
                if j == i:
                    j += 1
                cur_num = [nums[i], nums[j]]
                cur_gap = minus(val, cur_num)
                if cur_gap[0] == 0:
                    # step right
                    cover += l - j
                    i += 1
                    cur_lo = cur_num
                    lo_gap = [0, 0]
                    cur_hi = cur_num
                    hi_gap = [0, 0]
                elif cur_gap[0] > 0:
                    # step right
                    cover += l - j
                    i += 1
                    cur_lo_gap = cur_gap
                    if minus(cur_lo_gap, lo_gap)[0] < 0:
                        cur_lo = cur_num
                        lo_gap = cur_lo_gap
                else:
                    # step up
                    j += 1
                    cur_hi_gap = [-cur_gap[0], cur_gap[1]]
                    if minus(cur_hi_gap, hi_gap)[0] < 0:
                        cur_hi = cur_num
                        hi_gap = cur_hi_gap
            hi_cover = cover if lo_gap[0] == 0 else cover + 1
            return cur_lo + [cover], cur_hi + [hi_cover]

        lo = lo_all + [1]
        hi = hi_all + [l * (l - 1) / 2]

        # binary search
        while minus(hi, lo)[0] > 0:

            mi = ave(hi, lo)
            num1, num2 = search(A, mi)

            if num1[2] == K:
                return num1[:2]
            if num2[2] == K:
                return num2[:2]
            if num1[2] > K:
                hi = num1
            else:
                lo = num2

        return lo[:2]
