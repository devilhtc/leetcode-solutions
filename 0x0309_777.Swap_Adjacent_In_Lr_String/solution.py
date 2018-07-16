class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        a, b = [], []
        for i in range(len(start)):
            if start[i] != "X":
                a.append((start[i], i))
            if end[i] != "X":
                b.append((end[i], i))

        if "".join(e[0] for e in a) != "".join(e[0] for e in b):
            return False
        for i in range(len(a)):
            if a[i][0] == "L":
                if b[i][1] > a[i][1]:
                    return False
            else:
                if b[i][1] < a[i][1]:
                    return False
        return True
