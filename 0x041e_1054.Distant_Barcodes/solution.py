class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        l = len(barcodes)
        x = sorted(
            [[k, v] for k, v in collections.Counter(barcodes).items()],
            key=lambda x: -x[1],
        )
        k = 0
        j = 0
        out = [0] * l
        for i in range(l):
            out[j] = x[k][0]
            x[k][1] -= 1
            if x[k][1] == 0:
                k += 1
            j += 2
            if j >= l:
                j = 1
        return out
