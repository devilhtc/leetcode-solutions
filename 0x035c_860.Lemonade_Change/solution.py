class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        d = collections.defaultdict(int)
        for b in bills:
            if b == 5:
                d[5] = d[5] + 1
            elif b == 10:
                if d[5] > 0:
                    d[5] = d[5] - 1
                    d[10] = d[10] + 1
                else:
                    return False
            elif b == 20:
                if d[10] > 0 and d[5] > 0:
                    d[10] = d[10] - 1
                    d[5] = d[5] - 1
                elif d[5] > 2:
                    d[5] = d[5] - 3
                else:
                    return False
        return True
            
        