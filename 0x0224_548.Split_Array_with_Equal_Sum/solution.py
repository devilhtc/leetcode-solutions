class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        d = {}
        cs = 0
        css = [cs]
        for i, v in enumerate(nums):
            cs += v
            css.append(cs)
            if i != l - 1:
                d[(cs, v)] = i

        for i in range(1, l):
            for j in range(i + 2, l):
                si = css[i]
                sj = css[j] - css[i + 1]
                if si != sj:
                    continue
                rem_sum = css[-1] - css[j + 1]
                kv = rem_sum - 2 * sj
                ks = css[j + 1] + si + kv
                k = d.get((ks, kv), -1)
                if k > j + 1:
                    return True
        return False
