ranges = [
    (2000, 2017),
    (0, 12),
    (0, 31),
    (0, 23),
    (0, 59),
    (0, 59)
]
levels = {
    'Year': 0,
    'Month': 1,
    'Day': 2,
    'Hour': 3,
    'Minute': 4,
    'Second': 5
}


class DLTN:
    def __init__(self, k, v):
        self.k = k
        self.vs = [v]
        self.p = None
        self.n = None
        self.l = None
        self.r = None
    
    def insert(self, k, v):
        if k < self.k:
            if self.l is None:
                self.l = DLTN(k, v)
                return self.l
            else:
                return self.l.insert(k, v)
        else:
            if self.r is None:
                self.r = DLTN(k, v)
                return self.r
            else:
                return self.r.insert(k, v)
    
class DLLT:
    def __init__(self):
        self.root = None
        self.head = None
        self.tail = None
        self.k2node = {}
    
    def insert(self, k, v):
        if self.root is None:
            self.root = DLTN(k, v)
            self.head = self.root
            self.tail = self.root
            self.k2node[k] = self.root
            return
        
        if k in self.k2node:
            self.k2node.vs.append(v)
            return
        
        # key is not found
        cur = self.root
        l_closest = None
        if not k < self.head.k:
            while cur is not None:
                if cur.k < k:
                    if l_closest is None:
                        l_closest = cur
                    else:
                        if l_closest.k < cur.k:
                            l_closest = cur
                    cur = cur.r
                else:
                    cur = cur.l
                    
        cur = self.root
        r_closest = None
        if not k > self.tail.k:
            while cur is not None:
                if cur.k > k:
                    if r_closest is None:
                        r_closest = cur
                    else:
                        if r_closest.k > cur.k:
                            r_closest = cur
                    cur = cur.l
                else:
                    cur = cur.r
                    
        new_node = self.root.insert(k, v)
        self.k2node[k] = new_node
        if not l_closest:
            prev_head = self.head
            self.head = new_node
            new_node.n = prev_head
            prev_head.p = new_node
        elif not r_closest:
            prev_tail = self.tail
            self.tail = new_node
            new_node.p = prev_tail
            prev_tail.n = new_node
        else:
            l_closest.n = new_node
            new_node.p = l_closest
            r_closest.p = new_node
            new_node.n = r_closest
    
    def range_query(self, s, e):
        if s > e or self.root is None:
            return []
        if s == e:
            if s in self.k2node:
                return list(self.k2node[k].vs)
            return []
        snode = None
        if s in self.k2node:
            snode = self.k2node[s]
        else:
            node = self.root
            while node is not None:
                if node.k > s:
                    if snode is None:
                        snode = node
                    else:
                        if node.k < snode.k:
                            snode = node
                    node = node.l
                else:
                    node = node.r
        enode = None
        if e in self.k2node:
            enode = self.k2node[e]
        else:
            node = self.root
            while node is not None:
                if node.k < e:
                    if enode is None:
                        enode = node
                    else:
                        if node.k > enode.k:
                            enode = node
                    node = node.r
                else:
                    node = node.l
            
        if snode is None and enode is None:
            return []
        if snode is None or enode is None:
            return []
        if snode.k > enode.k:
            return []
        out = []
        node = snode
        while node and node.k != enode.k:
            for v in node.vs:
                out.append(v)
            node = node.n
        for v in enode.vs:
            out.append(v)
        return out
                    
    
class LogSystem:
    def __init__(self):
        self.dllt = DLLT()

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        k = self._ts2k(timestamp)
        self.dllt.insert(k, id)

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        sk, ek = self._ts2k(s), self._ts2k(e)
        sk = self._truncate(sk, gra, True)
        ek = self._truncate(ek, gra, False)
        return self.dllt.range_query(sk, ek)

    def _ts2k(self, ts):
        return tuple([int(ele) for ele in ts.split(':')])
        
    def _truncate(self, k, gra, to_start):
        i = levels[gra]
        out = []
        for j in range(i + 1):
            out.append(k[j])
        for j in range(i + 1, 6):
            out.append(ranges[j][0 if to_start else 1])
        return tuple(out)

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)