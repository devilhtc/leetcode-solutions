class Solution:
    def countTriplets(self, A: "List[int]") -> "int":
        d = collections.defaultdict(int)
        l = len(A)
        for i in range(l):
            for j in range(l):
                d[A[i] & A[j]] += 1

        out = 0
        for i in range(l):
            for k, v in d.items():
                if A[i] & k == 0:
                    out += v
        return out
