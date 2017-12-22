def getNext(numRows, cur, direction):
    if cur == numRows - 1 and direction == 1:
        return cur - 1, -1
    if cur == 0 and direction == -1:
        return 1, 1
    return cur + direction, direction

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        cur = 0
        direction = 1
        for i in range(len(s)):
            rows[cur].append(s[i])
            cur, direction = getNext(numRows, cur, direction)
        out = ''.join([''.join(row) for row in rows])
        return out