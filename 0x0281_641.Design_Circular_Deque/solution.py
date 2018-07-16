class Node(object):
    """
    Doubly-linked list node
    """
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

        
class MyCircularDeque(object):
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.cap = k
        self.size = 0
        self.head = None
        self.tail = None      

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size == self.cap:
            return False
        
        node = Node(value)
        
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node   
        
        self.size += 1
        return True
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size == self.cap:
            return False
        
        node = Node(value)
        
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        
        self.size += 1 
        return True
        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size == 0:
            return False
        
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            prevhead = self.head
            self.head = self.head.next
            self.head.prev = None
        
        self.size -= 1
        return True
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size == 0:
            return False
        
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            prevtail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.size -= 1
        return True
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.size == 0:
            return -1
        
        return self.head.val
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.size == 0:
            return -1
        
        return self.tail.val
    

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.size == 0
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.size == self.cap


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()