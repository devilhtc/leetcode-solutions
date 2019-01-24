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
    def __init__(self):
        """
        :type capacity: int
        """
        self.size = 0
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
        value = n.v
        if n == self.head:
            return value
        self.remove(key)
        self.add(key, value)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.k2n:
            self.remove(key)
        self.add(key, value)

    def remove(self, key):
        node = self.k2n.pop(key)
        p, n = node.rm()
        if node == self.head:
            self.head = n
        if node == self.tail:
            self.tail = p
        self.size -= 1

    def add(self, key, value):
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

    def evict(self):
        node = self.tail
        self.k2n.pop(node.k)
        self.tail = node.p
        node.rm()
        self.size -= 1
        return self.size == 0


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class CountNode:
    def __init__(self, count):
        self.count = count
        self.lru = LRUCache()
        self.prev = None
        self.next = None

    def __repr__(self):
        lru_nodes = []
        node = self.lru.head
        while node:
            lru_nodes.append("<DLN {}:{}>".format(node.k, node.v))
            node = node.n
        return "<CountNode({}) of size {}: {}>".format(
            self.count, self.lru.size, lru_nodes
        )


class LFUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.count2node = {}
        self.key2count = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2count:
            return -1

        count = self.key2count[key]
        count_node = self.count2node[count]
        value = count_node.lru.get(key)
        self.promote(key)
        return value

    def put(self, key, value):

        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        if key not in self.key2count:
            self.size += 1
            # evict
            if self.size > self.capacity:
                dln = self.tail.lru.tail
                key2 = dln.k
                self.tail.lru.remove(key2)
                tail_size = self.tail.lru.size

                tail_count = self.key2count.pop(key2)
                if tail_size == 0:
                    # need to evict tail node as well
                    if self.tail == self.head:
                        self.tail = None
                        self.head = None
                    else:
                        new_tail = self.tail.prev
                        new_tail.next = None
                        self.tail = new_tail
                    self.count2node.pop(tail_count)

                self.size -= 1

            self.key2count[key] = 1
            if 1 not in self.count2node:
                count_node = CountNode(1)
                count_node.lru.put(key, value)
                if self.head is None and self.tail is None:
                    self.head = count_node
                    self.tail = count_node
                else:
                    old_tail = self.tail
                    old_tail.next = count_node
                    count_node.prev = old_tail
                    self.tail = count_node
                self.count2node[1] = count_node
            else:
                count_node = self.count2node[1]
                count_node.lru.put(key, value)

        else:
            count_node = self.count2node[self.key2count[key]]
            count_node.lru.put(key, value)
            self.promote(key)

    def promote(self, key):
        current_count = self.key2count[key]
        current_node = self.count2node[current_count]
        value = current_node.lru.get(key)
        current_node.lru.remove(key)

        # add it to a count_node
        if current_node == self.head:  # already the maximum count
            new_node = CountNode(current_count + 1)
            new_node.lru.put(key, value)
            new_node.next = current_node
            current_node.prev = new_node
            self.head = new_node
            self.count2node[current_count + 1] = new_node
        else:
            # look ahead
            p = current_node.prev
            if p.count == current_count + 1:
                p.lru.put(key, value)
            else:
                new_node = CountNode(current_count + 1)
                new_node.lru.put(key, value)
                new_node.prev = p
                new_node.next = current_node
                p.next = new_node
                current_node.prev = new_node
                self.count2node[current_count + 1] = new_node

        self.key2count[key] = current_count + 1

        if current_node.lru.size == 0:
            # current node needs to be evicted
            self.count2node.pop(current_count)
            if current_node is self.tail:
                p = self.tail.prev
                p.next = None
                self.tail = p
            else:
                p, n = current_node.prev, current_node.next
                if p:
                    p.next = n
                if n:
                    n.prev = p


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
