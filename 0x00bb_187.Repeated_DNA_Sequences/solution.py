class Solution:
    def findRepeatedDnaSequences(self, s: "str") -> "List[str]":
        v = set()
        dq = collections.deque([])
        out = set()
        for i, c in enumerate(s):
            dq.append(c)
            if i < 9:
                continue
            seq = "".join(list(dq))
            if seq in v:
                out.add(seq)
            v.add(seq)
            dq.popleft()
        return list(out)
