class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0 or k == 0:
            return 0
        d = collections.defaultdict(int)
        d[s[0]] = 1
        n = 1
        j = 1
        i = 0
        l = len(s)
        out = 1
        while i < len(s):
            while j < len(s):
                c2 = s[j]
                # try adding it to d
                # if fails, bt
                d[c2] += 1
                if d[c2] == 1:
                    n += 1
                if n > k:
                    d[c2] -= 1
                    n -= 1
                    break
                else:
                    j += 1
            out = max(out, j - i)
            c = s[i]
            d[c] -= 1
            if d[c] == 0:
                n -= 1
            i += 1
        return out
