class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}
        i = 0
        ml = 0
        for j in range(len(s)):
            # take in the jth character
            # increase i until counts[s[i]] = 1
            # length is then j - i + 1
            counts[s[j]] = counts.get(s[j], 0) + 1
            while counts[s[j]] > 1:
                counts[s[i]] -= 1
                i += 1
            ml = max(j - i + 1, ml)
        return ml
