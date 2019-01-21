class DLN:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.p = None
        self.n = None

    def rm(self):
        p, n = self.p, self.n
        if self.p:
            self.p.n = self.n
        if self.n:
            self.n.p = self.p
        self.p = None
        self.n = None
        return p, n


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.k2n = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.k2n:
            return -1
        n = self.k2n[key]
        out = n.v
        if n == self.head:
            return out
        self._remove(key)
        self._add(key, out)
        return out

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.k2n:
            self._remove(key)
        self._add(key, value)
        if self.size > self.capacity:
            self._evict()

    def _remove(self, key):
        node = self.k2n.pop(key)
        p, n = node.rm()
        if node == self.head:
            self.head = n
        if node == self.tail:
            self.tail = p
        self.size -= 1

    def _add(self, key, value):
        node = DLN(key, value)
        self.k2n[key] = node
        if self.head:
            old_head = self.head
            self.head = node
            node.n = old_head
            old_head.p = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def _evict(self):
        node = self.tail
        self.k2n.pop(node.k)
        self.tail = node.p
        node.rm()
        self.size -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
