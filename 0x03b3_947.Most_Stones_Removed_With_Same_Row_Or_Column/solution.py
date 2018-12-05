class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        uf = {}
        Y_OFFSET = 10001

        def union(i, j):
            j = j + Y_OFFSET
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

        for s in stones:
            union(*s)
        return len(stones) - len(set(find[ele] for ele in uf))
