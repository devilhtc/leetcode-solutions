# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        nodes = []
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next
        fakehead = ListNode(0)
        prev = fakehead
        i, j = 0, len(nodes) - 1
        while i <= j:
            cur1 = nodes[i]
            cur2 = nodes[j]
            prev.next = cur1
            cur1.next = cur2
            cur2.next = None
            prev = cur2
            i += 1
            j -= 1
