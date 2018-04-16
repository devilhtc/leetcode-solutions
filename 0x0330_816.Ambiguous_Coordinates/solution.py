import itertools

class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S[1:-1]
        comb = lambda x: '(' + x[0] + ', ' + x[1] + ')'
        out = []
        for i in range(1, len(S)):
            for a, b in itertools.product(self.ways(S[:i]), self.ways(S[i:])):
                out.append(comb((a, b)))
        return out
    
    def ways(self, ds):
        if len(ds) == 0: return []
        if len(ds) == 1: return [ds]
        if ds[0] == '0' and ds[-1] == '0': return []
        if ds[0] == '0': return [ds[0] + '.' + ds[1:]]
        if ds[-1] == '0': return [ds]
        return [ds[:i] + '.' + ds[i:] for i in range(1, len(ds))] + [ds]
        