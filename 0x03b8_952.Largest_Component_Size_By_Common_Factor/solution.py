class Solution:
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
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

        def find_prime_facs(n):
            list_of_factors = []
            i = 2
            while n > 1:
                if n % i == 0:
                    list_of_factors.append(i)
                    n = n // i
                    i = i - 1
                i += 1
                if i > math.sqrt(n) + 1:
                    if n > 1:
                        list_of_factors.append(n)
                    break
            return list_of_factors

        f2n = collections.defaultdict(set)
        for v in A:
            facs = find_prime_facs(v)
            for f in facs:
                f2n[f].add(v)

        # print(f2n)
        for f, vs in f2n.items():
            x = vs.pop()
            for v in vs:
                union(x, v)
        # print(uf)

        fc = collections.defaultdict(int)
        for v in A:
            fc[find(v)] += 1
        # print(fc)
        return max(c for _, c in fc.items())
