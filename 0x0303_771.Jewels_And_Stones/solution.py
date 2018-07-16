class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        s = set(list(J))
        count = 0
        for c in S:
            if c in s:
                count += 1
        return count
