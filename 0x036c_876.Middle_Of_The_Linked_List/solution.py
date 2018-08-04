# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = self.getLen(head)
        return self.getNode(head, l // 2)

    def getLen(self, node):
        # get the length of a singly linked list
        if node is None:
            return 0
        return self.getLen(node.next) + 1

    def getNode(self, node, n):
        # get the n-th node of a singly linked list
        if n == 0:
            return node
        return self.getNode(node.next, n - 1)
