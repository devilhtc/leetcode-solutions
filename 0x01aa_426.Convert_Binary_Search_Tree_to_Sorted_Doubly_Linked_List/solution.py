"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.head = None
        self.cur = None
        self.tail = None
        self.inorder(root)
        if self.head is not None:
            self.tail.right = self.head
            self.head.left = self.tail
        return self.head

    def inorder(self, node):
        if node is None:
            return
        l, r = node.left, node.right
        node.left = None
        node.right = None

        self.inorder(l)

        if self.head is None:
            self.head = node
            self.cur = node
        else:
            self.cur.right = node
            node.left = self.cur
            self.cur = node

        self.tail = node

        self.inorder(r)
