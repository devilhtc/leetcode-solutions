class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def nbadd(a, b, c):
            k = a + b + c
            if k == -1:
                return 1, 1
            return k % 2, -1 if k >= 2 else 0

        c = 0
        out = []
        for i in range(max(len(arr1), len(arr2))):
            a = arr1[-(i + 1)] if i < len(arr1) else 0
            b = arr2[-(i + 1)] if i < len(arr2) else 0
            k, c = nbadd(a, b, c)
            out.append(k)
        if c == 1:
            out.append(1)
        elif c == -1:
            out.append(1)
            out.append(1)
        elif c == 0:
            while len(out) > 1 and out[-1] == 0:
                out.pop()
        return list(reversed(out))
