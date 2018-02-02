from collections import Counter

# Counter solution: can use counter.most_common(m) method
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        ctr = Counter(S)
        if ctr.most_common(1)[0][1] > (len(S) + 1)/2: return ""
        out = []
        for i in range(len(S)):
            mc = ctr.most_common(2)
            c = mc[0][0]
            if len(out) > 0:
                if c == out[-1]:
                    c = mc[1][0]
            out.append(c)
            ctr.subtract(Counter(c))
        return ''.join(out)          
                