# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.addTwoHelper(l1, l2, 0)

    def addTwoHelper(self, l1, l2, carry):
        if l1 is None and l2 is None:
            if carry == 0:
                return None
            else:
                return ListNode(1)
        if l1 is None:
            if l2.val + carry == 10:
                l2.val = 0
                l2.next = self.addTwoHelper(None, l2.next, 1)
                return l2
            else:
                l2.val += carry
                return l2
        if l2 is None:
            return self.addTwoHelper(l2, l1, carry)

        curVal = l1.val + l2.val + carry
        node = ListNode(curVal % 10)
        node.next = self.addTwoHelper(l1.next, l2.next, curVal / 10)
        return node
