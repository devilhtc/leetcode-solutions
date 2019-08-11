class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        mf = 0  # maximum of customers flipped
        cf = 0  # current number of customers flipped
        p = 0
        l = len(customers)
        for i in range(l):
            if i - p == X:
                if grumpy[p]:
                    cf -= customers[p]
                p += 1
            if grumpy[i]:
                cf += customers[i]
            mf = max(mf, cf)

        return sum(customers[i] for i in range(l) if not grumpy[i]) + mf
