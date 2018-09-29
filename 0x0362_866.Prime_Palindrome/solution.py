class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        if 8 <= N <= 11: return 11
        Ns = str(N)
        l = len(Ns)
        start = (10 ** (l // 2)) if (l % 2 == 0) else (int(Ns[:(l + 1)//2]) - 1)
        for i in range(start, 100000):
            num = int(str(i) + ''.join(list(reversed(str(i)))[1:]))
            if num >= N and self.isPrime(num):
                return num
        return num
    
    def isPrime(self, s):
        if s < 2:
            return False
        if s == 2:
            return True
        i = 2
        while i * i <= s:
            if s % i == 0:
                return False
            i += 1
        return True