class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        count = 0
        d = {}
        for a in answers:
            d[a] = d.get(a, 0) + 1
            if d[a] == a + 1:
                count += a + 1
                d[a] = 0
        for k in d:
            if d[k] != 0:
                count += k + 1
        return count
