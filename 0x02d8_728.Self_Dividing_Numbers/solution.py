class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isSD(a, b):
            if a == 0: return True
            c = a % 10
            if c == 0:
                return False
            if b % c != 0:
                return False
            else:
                return isSD(a/10, b)
        
        out = []
        for i in range(left, right + 1):
            if isSD(i, i):
                out.append(i)
        return out
            
        