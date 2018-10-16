class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        ds = list(dominoes)
        i = 0  # num resolved
        while i < len(ds):
            if ds[i] == "L":
                i += 1
                continue

            j, ns = self.getNextStop(ds, i)

            if ns is None:
                # reached the end
                if ds[i] == "R":
                    # resolve to right iff current is R
                    for k in range(i + 1, len(ds)):
                        ds[k] = "R"
                i = j
                continue

            if ds[i] == "." and ns == "L":
                # resolve to left
                for k in range(i, j):
                    ds[k] = "L"
                i = j + 1
            elif ds[i] == "." and ns == "R":
                # no falling, skip to j
                i = j
            elif ds[i] == "R" and ns == "L":
                # resolve to the middle
                l, r = i, j
                while l < r:
                    ds[l] = "R"
                    ds[r] = "L"
                    l += 1
                    r -= 1
                i = j + 1
            elif ds[i] == "R" and ns == "R":
                for k in range(i, j):
                    ds[k] = "R"
                i = j
        return "".join(ds)

    def getNextStop(self, ds, i):
        for j in range(i + 1, len(ds)):
            if ds[j] != ".":
                return j, ds[j]
        else:
            return len(ds), None
