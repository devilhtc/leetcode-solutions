# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None

        # spawn new nodes following old nodes
        node = head
        while node is not None:
            n = node.next
            node.next = RandomListNode(node.label)
            node.next.next = n
            node = n
        
        # populate random pointer of new nodes
        node = head
        while node is not None:
            n = node.next.next
            if node.random is not None:
                node.next.random = node.random.next
            node = n

        out = head.next
        node = head
        while node is not None:
            n = node.next.next
            n2 = node.next
            node.next = n
            if n is not None:
                n2.next = n.next
            node = n
        
        return out
   
        