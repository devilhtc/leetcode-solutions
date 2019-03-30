class Solution:
    def queryString(self, S: str, N: int) -> bool:
        def num2bs(num):
            return "{:b}".format(num)

        bsN = num2bs(N)
        l = len(bsN)
        # check for longest then shortest -> fail early
        for j in range(N, 0, -1):
            bs = num2bs(j)
            if bs not in S:
                return False
            # early stopping, since the
            # numbers with binary repr length l - 1
            # should have covered all the l - 2 ones
            # and so on - so all are covered
            if len(bs) < l - 1:
                return True
        return True
