# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: "ListNode", k: "int") -> "ListNode":
        def getlen(node):
            i = 0
            while node:
                i += 1
                node = node.next
            return i

        def helper(node):
            if getlen(node) < k:
                return node, None, None
            p = None
            h = None
            t = None
            i = 0
            while i < k:
                n = node.next
                node.next = p
                if t is None:
                    t = node
                h = node
                p = node
                node = n
                i += 1
            return h, t, n

        nh = None
        nt = None
        while head:
            h, t, n = helper(head)
            if nh is None:
                nh = h
            if nt is not None:
                nt.next = h
            nt = t
            head = n

        return nh
