class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        negs = []
        zeros = []
        poss = []
        for ele in A:
            if ele < 0:
                negs.append(ele)
            elif ele == 0:
                zeros.append(ele)
            else:
                poss.append(ele)

        if K > len(negs):
            if len(zeros) > 0 or (K - len(negs)) % 2 == 0:
                return sum(poss) - sum(negs)
            else:
                if len(poss) == 0:
                    minVal = -max(negs)
                elif len(negs) == 0:
                    minVal = min(poss)
                else:
                    minVal = min(min(poss), -max(negs))
                return sum(poss) - sum(negs) - minVal * 2

        else:
            negs = sorted(negs)
            for i in range(K):
                negs[i] = -negs[i]
            return sum(poss) + sum(negs)
