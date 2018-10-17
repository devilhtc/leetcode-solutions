class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        isValid = [False] * l
        opens = []
        for i in range(l):
            if s[i] == "(":
                opens.append(i)
            else:
                if len(opens) > 0:
                    prev = opens.pop()
                    isValid[prev] = True
                    isValid[i] = True
        maxlen = 0
        curlen = 0
        for i in range(l):
            if isValid[i]:
                curlen += 1
                maxlen = max(maxlen, curlen)
            else:
                curlen = 0
        return maxlen
