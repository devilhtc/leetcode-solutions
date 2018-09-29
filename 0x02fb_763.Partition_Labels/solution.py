class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        e = {v: i for i, v in enumerate(S)}
        bp = []
        i = j = 0
        for k, v in enumerate(S):
            j = max(e[v], j)
            if j == k:
                bp.append(k)
                i = j = k + 1
        return [v - (-1 if i == 0 else bp[i - 1]) for i, v in enumerate(bp)]
