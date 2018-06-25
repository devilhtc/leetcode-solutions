import heapq

class Interval(object):
    """
    An interval in the exam room
    """

    def __init__(self, N, s, e):
        self.N = N # max of interval
        self.s = s # start of interval
        self.e = e # end of interval
        self.build()
    
    def build(self):
        seat, dis = self.get_seat_and_dis()
        self.seat = seat 
        self.dis = dis
        self.removed = False

    def get_seat_and_dis(self):
        if self.s == 0 and self.e == self.N - 1: # is the whole room - seat the student at 0
            seat = 0
            dis = self.N
        elif self.s == 0: # is at the start
            seat = 0
            dis = self.e + 1
        elif self.e == self.N - 1: # is at the end
            seat = self.e
            dis = self.e - self.s + 1
        else:
            seat = (self.s + self.e) / 2 # the position to seat to obtain max min dis
            dis = seat - self.s + 1
        return seat, dis
    
    def spawn_children(self):
        # start and end of interval after the split
        left = (self.s, self.seat - 1)
        right = (self.seat + 1, self.e)
        candidates = [left, right]
        # create interval if end >= start
        out = [Interval(self.N, c[0], c[1]) for c in candidates if c[1] >= c[0]]
        return out

    def __cmp__(self, other):
        if self.dis != other.dis:
            return other.dis - self.dis
        return self.seat - other.seat
    
    def __repr__(self):
        r = '<Interval [{}, {}] with N = {}>'.format(self.s, self.e, self.N)
        return '<Removed Interval>' if self.removed else r

    def remove(self):
        self.removed = True


"""
merge a list of adjacent intervals (might contain None)
contains at least 1 non-None element
"""
def merge_intervals(itvs):
    itvs = [ele for ele in itvs if ele is not None]
    N = itvs[0].N
    new_s = min(ele.s for ele in itvs)
    new_e = max(ele.e for ele in itvs)
    return Interval(N, new_s, new_e)


class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N 
        self.build()
    
    def build(self):
        itv = Interval(self.N, 0, self.N - 1)
        self.pq = [itv] # priority queue to keep track of intervals
        self.m = { 0: itv, self.N - 1: itv } # hashmap for merging

    def seat(self):
        """
        :rtype: int
        """
        # get the interval to be split
        seat, itv = 0, None
        while True and len(self.pq) > 0:
            itv = heapq.heappop(self.pq)
            if not itv.removed:
                break

        if itv is None:
            return -1

        # remove it from hashmap
        self.m.pop(itv.s)
        self.m.pop(itv.e)

        children = itv.spawn_children()

        for c in children:
            heapq.heappush(self.pq, c)
            self.m[c.s] = c
            self.m[c.e] = c

        return itv.seat

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        p_itv = Interval(self.N, p, p)
        to_merge = [p_itv]

        # remove the previous and next interval
        prev_itv = self.m.pop(p - 1, None)
        next_itv = self.m.pop(p + 1, None)
        if prev_itv is not None:
            self.m.pop(prev_itv.s, None)
            prev_itv.remove()
            to_merge.append(prev_itv)
        if next_itv is not None:
            self.m.pop(next_itv.e, None)
            next_itv.remove()
            to_merge.append(next_itv)

        merged = merge_intervals(to_merge)
        heapq.heappush(self.pq, merged)
        self.m[merged.s] = merged
        self.m[merged.e] = merged


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)

"""
def main():
    er = ExamRoom(20)
    for i in range(3):
        print i + 1
        print er.seat()
        print er.pq
        print er.m
        print 
    er.leave(9)
    print er.pq
    print er.m
    print 
    for i in range(3):
        print i 
        print er.seat()
        print er.pq
        print er.m
        print 

if __name__ == '__main__':
    main()
"""