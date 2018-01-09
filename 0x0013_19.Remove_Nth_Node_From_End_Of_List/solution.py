# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getlen(head):
    if head is None:
        return 0
    return 1 + getlen(head.next)

# given i <= getlen(head)
def getIth(head, i):
    if i == 1:
        return head
    return getIth(head.next, i - 1)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = getlen(head)
        if n > l:
            return head
        if n == l:
            return head.next
        indexToRemove = l - n + 1
        pre = getIth(head, indexToRemove - 1)
        cur = pre.next
        pre.next = cur.next
        return head
        
        