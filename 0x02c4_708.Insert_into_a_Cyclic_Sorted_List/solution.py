"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""


class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        a = Node(insertVal, None)
        if not head:
            a.next = a
            return a
        x, y = head, head.next
        while True:
            if (
                y is head
                or (x.val <= insertVal <= y.val)
                or (x.val > y.val and (insertVal <= y.val or insertVal >= x.val))
            ):
                x.next = a
                a.next = y
                break
            x, y = x.next, y.next
        return head
