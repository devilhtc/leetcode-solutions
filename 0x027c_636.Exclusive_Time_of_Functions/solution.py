class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        out = [0] * n
        t = 0
        m = 0
        for l in logs:
            fid, se, ts = l.split(":")
            fid = int(fid)
            ts = int(ts)
            if se == "start":
                if len(stack) > 0:
                    out[stack[-1]] += ts - t - m
                t = ts
                m = 0
                stack.append(fid)
            else:
                out[stack.pop()] += ts - t + 1 - m
                t = ts
                m = 1
        return out
