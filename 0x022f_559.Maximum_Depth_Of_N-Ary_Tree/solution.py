"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return (
            max(self.maxDepth(ele) for ele in root.children + [None]) + 1
            if root is not None
            else 0
        )
