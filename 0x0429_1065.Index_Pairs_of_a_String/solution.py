class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        out = []
        for word in words:
            s = 0
            k = text.find(word, s)
            while k != -1:
                out.append([k, k + len(word) - 1])
                s = k + 1
                k = text.find(word, s)
        return sorted(out)
