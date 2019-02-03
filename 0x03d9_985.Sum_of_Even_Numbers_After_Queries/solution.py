class Solution:
    def sumEvenAfterQueries(
        self, A: "List[int]", queries: "List[List[int]]"
    ) -> "List[int]":
        esum = sum([ele for ele in A if ele % 2 == 0])
        out = []
        for val, i in queries:
            pval = A[i]
            nval = A[i] + val
            if pval % 2 == 0:
                esum -= pval
            if nval % 2 == 0:
                esum += nval
            A[i] = nval
            out.append(esum)
        return out
