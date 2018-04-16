# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        s = set(G)
        c = 0
        out = 0
        node = head
        while node is not None:
            if node.val in s:
                c += 1
                if c == 1: out += 1
            else:
                c = 0
            node = node.next
        return out
        