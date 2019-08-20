class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s = set(source)
        for c in target:
            if c not in s:
                return -1
        i = 0
        j = 0
        out = 0
        while i < len(target):
            if source[j] == target[i]:
                i += 1
            j += 1
            if j == len(source):
                j = 0
                out += 1
        return out + (1 if j > 0 else 0)
