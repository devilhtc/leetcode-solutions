class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """

        cts = {"0": 0, "1": 0}
        for c in S:
            cts[c] += 1

        out = cts["0"]
        cur = {"0": 0, "1": 0}
        for c in S:
            cur[c] += 1
            out = min(out, (cur["1"]) + (cts["0"] - cur["0"]))
        return out
