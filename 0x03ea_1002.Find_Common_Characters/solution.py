class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) == 0:
            return []
        counters = [collections.Counter(s) for s in A]
        x = set(counters[0].keys())  # common characters
        for i in range(1, len(counters)):
            x = x & set(counters[i].keys())
        y = {c: min(counter[c] for counter in counters) for c in x}
        out = []
        for k, v in y.items():
            for _ in range(v):
                out.append(k)
        return out
