# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        fakehead = ListNode(0)
        prev = fakehead
        cur = head
        while True:
            if cur and cur.next:
                n1 = cur
                n2 = cur.next
                n3 = cur.next.next
                prev.next = n2
                n2.next = n1
                n1.next = None
                prev = n1
                cur = n3
            else:
                if cur:
                    prev.next = cur
                break
        return fakehead.next
