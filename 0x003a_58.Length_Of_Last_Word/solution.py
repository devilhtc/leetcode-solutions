class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = s.strip().split()
        if len(ss) == 0:
            return 0
        return len(ss[-1])
