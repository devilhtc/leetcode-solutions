# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def getlen(node):
    if node is None:
        return 0
    else:
        return getlen(node.next) + 1


def getnode(node, k):
    if k == 0:
        return node
    else:
        return getnode(node.next, k - 1)


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        l = getlen(root)
        lengths = [0 for _ in range(k)]
        for i in range(l):
            lengths[i % k] += 1
        out = []
        head = root
        for i in range(k):
            curlen = lengths[i]
            if curlen == 0:
                out.append(None)
            else:
                out.append(head)
                tail = getnode(head, curlen - 1)

                head = getnode(head, curlen)
                tail.next = None
        return out
