class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        uf = {}

        def union(i, j):
            fi = find(i)
            fj = find(j)
            if fi == fj:
                return
            if fi > fj:
                fi, fj = fj, fi
            uf[fj] = fi

        def find(i):
            if i not in uf:
                uf[i] = i
            j = i
            while uf[j] != j:
                j = uf[j]
            uf[i] = j
            return j

        for a, b in zip(A, B):
            union(a, b)

        return "".join(find(c) for c in S)
