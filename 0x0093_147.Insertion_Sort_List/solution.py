# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        fakehead = ListNode(0)

        node = head
        while node is not None:
            n = node.next
            node.next = None
            # insert
            self.insert(fakehead, node)
            node = n
        return fakehead.next

    def insert(self, fakehead, node):
        prev = fakehead
        cur = fakehead.next
        while cur is not None and cur.val < node.val:
            prev = cur
            cur = prev.next
        prev.next = node
        node.next = cur
