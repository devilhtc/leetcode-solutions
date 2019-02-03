# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def findlen(node):
            if node is None:
                return 0
            l = 0
            cur = node
            while cur is not None:
                cur = cur.next
                l += 1
            return l

        def addhelper(node1, node2, len1, len2):
            if len2 > len1:
                return addhelper(node2, node1, len2, len1)
            if len1 > len2:
                curval = node1.val
                nextnode, carry = addhelper(node1.next, node2, len1 - 1, len2)
                curval = carry + curval
                curcarry = 0
                if curval >= 10:
                    curcarry = 1
                    curval = curval - 10
                curnode = ListNode(curval)
                curnode.next = nextnode
                return curnode, curcarry
            if len1 == 0 and len2 == 0:
                return None, 0
            nextnode, carry = addhelper(node1.next, node2.next, len1 - 1, len2 - 1)
            curval = node1.val + node2.val + carry
            curcarry = 0
            if curval >= 10:
                curcarry = 1
                curval = curval - 10
            curnode = ListNode(curval)
            curnode.next = nextnode
            return curnode, curcarry

        len1 = findlen(l1)
        len2 = findlen(l2)
        nextnode, carry = addhelper(l1, l2, len1, len2)
        if carry:
            head = ListNode(1)
            head.next = nextnode
        else:
            head = nextnode

        return head
