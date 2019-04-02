# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        out = []
        stack = []
        node = head
        i = 0
        while node is not None:
            while len(stack) > 0 and node.val > stack[-1][0]:
                v, j = stack.pop()
                out[j] = node.val
            stack.append((node.val, i))
            out.append(0)
            i += 1
            node = node.next
        return out
