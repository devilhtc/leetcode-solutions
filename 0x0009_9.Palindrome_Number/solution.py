class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        l = self.getLen(x)
        rightPart = 0
        leftPart = x
        for i in range(l / 2):
            rightPart = rightPart * 10 + self.getIth(x, i)
            leftPart /= 10
        if l % 2 == 0:
            return leftPart == rightPart
        else:
            return leftPart / 10 == rightPart

    def getLen(self, x):
        l = 0
        while x > 0:
            x /= 10
            l += 1
        return l

    def getIth(self, x, i):
        for k in range(i):
            x /= 10
        return x % 10
