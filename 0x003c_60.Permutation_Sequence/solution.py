FAC = [1]
for i in range(9):
    FAC.append(FAC[-1] * (i + 1))
    
class Solution:
    
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return "1"
        fd = (k - 1) // (FAC[n - 1]) + 1
        res = (k - 1) % (FAC[n - 1]) + 1
        perm = self.getPermutation(n - 1, res)
        out = [str(fd)]
        for c in perm:
            out.append(str(int(c) + (1 if int(c) >= fd else 0)))
        return ''.join(out)
                