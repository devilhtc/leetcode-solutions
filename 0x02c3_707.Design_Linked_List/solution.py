class LLN:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if not 0 <= index < self.size:
            return -1
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = LLN(val)
        self.size += 1
        if self.head is None:
            self.head = self.tail = node
            return
        self.head.prev = node
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = LLN(val)
        self.size += 1
        if self.tail is None:
            self.head = self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if not 0 <= index <= self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        node = LLN(val)
        self.size += 1
        a, b = self.head, self.head.next
        while index > 1:
            a, b = a.next, b.next
            index -= 1
        a.next = node
        node.prev = a
        node.next = b
        b.prev = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if not 0 <= index < self.size:
            return
        if index == 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head.next.prev = None
                self.head = self.head.next
        elif index == self.size - 1:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.tail.prev.next = None
                self.tail = self.tail.prev
        else:
            cur = self.head
            while index > 0:
                cur = cur.next
                index -= 1
            p = cur.prev
            n = cur.next
            p.next = n
            n.prev = p
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
