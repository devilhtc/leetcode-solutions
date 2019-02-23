# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: "ListNode") -> "ListNode":
        prev = None
        newHead = None
        while head:
            n = head.next
            head.next = prev
            prev = head
            newHead = head
            head = n
        return newHead
