class Solution:
    def subarraysWithKDistinct(self, A: "List[int]", K: "int") -> "int":
        d1, c1, j1 = collections.defaultdict(int), 0, 0
        d2, c2, j2 = collections.defaultdict(int), 0, 0
        out = 0
        l = len(A)

        for v in A:
            # suppose current index is i

            # increament j1 so the subarray i:j1 has K distinct elements
            # with smallest j1
            while j1 < l and c1 < K:
                d1[A[j1]] += 1
                if d1[A[j1]] == 1:
                    c1 += 1
                j1 += 1

            # increament j2 so the subarray i:j1 has K distinct elements
            # with largest j2
            while j2 < l:
                if c2 == K and d2.get(A[j2], 0) == 0:
                    break
                d2[A[j2]] += 1
                if d2[A[j2]] == 1:
                    c2 += 1
                j2 += 1

            # add to output if there are K distinct elements
            # c1 and c2 can be < K when i is at the end of the array
            if c1 == K:
                out += j2 - j1 + 1

            # remove the current element, prepare for next iteration
            d1[v] -= 1
            if d1[v] == 0:
                c1 -= 1
            d2[v] -= 1
            if d2[v] == 0:
                c2 -= 1

        return out
