# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        def getlen(node):
            l = 0
            while node:
                l += 1
                node = node.next
            return l

        l1 = getlen(headA)
        l2 = getlen(headB)

        while l1 != l2:
            if l1 > l2:
                headA = headA.next
                l1 -= 1
            else:
                headB = headB.next
                l2 -= 1

        while headA:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None
