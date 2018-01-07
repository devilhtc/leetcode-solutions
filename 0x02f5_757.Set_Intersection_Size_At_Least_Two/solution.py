class Tracker(object):
    def __init__(self):
        self.d = {}
        self.q0 = []
        self.q1 = []
        self.s = set([])
    
    def addInterval(self, itv):
        self.d[itv] = 0
        self.q0.append(itv)
        
    def addPoint(self, cur):
        if cur in self.s: return 
        q1l, q0l, q1n = [], [], []
        for itv in self.q1:
            if itv[0] <= cur:
                self.d[itv] = 2
            else:
                q1l.append(itv)
        for itv in self.q0:
            if itv[0] <= cur:
                self.d[itv] = 1
                q1n.append(itv)
            else:
                q0l.append(itv)
        self.q1 = q1l + q1n
        self.q0 = q0l
        self.s.add(cur)
        
class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        whole = sorted(list(set([(ele[0], -1, (ele[0], ele[1])) for ele in intervals] + [(ele[1], 1, (ele[0], ele[1])) for ele in intervals])))
        t = Tracker()
        for cur, pos, itv in whole:
            if pos == -1: # start of interval, just append
                t.addInterval(itv)
            else: # end of interval, 
                # check if it already intersected by more than 2
                if t.d[itv] < 2: # add the current point if not enough
                    t.addPoint(cur)
                    if t.d[itv] == 1: # add cur - 1 if still not enough
                        t.addPoint(cur - 1)
        return len(t.s)