class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs) // 2
        base = 0
        A, B = [], []
        eq = 0
        for a, b in costs:
            base += min(a, b)
            if a > b:
                A.append(a - b)
            elif b > a:
                B.append(b - a)
            else:
                eq += 1

        def calc_surplus(l):
            l.sort()
            out = 0
            for i in range(len(l) - N):
                out += l[i]
            return out

        if len(A) > N:
            base += calc_surplus(A)
        elif len(B) > N:
            base += calc_surplus(B)
        return base
