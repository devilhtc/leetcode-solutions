class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        l = len(words)
        words = sorted(words, key=len)

        def has_edge(i, j):
            wi = words[i]
            wj = words[j]
            if len(wi) != len(wj) - 1:
                return False
            k = 0
            for c in wj:
                if c == wi[k]:
                    k += 1
                if len(wi) == k:
                    return True
            return False

        longest = [1] * l
        for i in range(l):
            for j in range(i + 1, l):
                if has_edge(i, j):
                    longest[j] = max(longest[j], longest[i] + 1)

        return max(longest)
