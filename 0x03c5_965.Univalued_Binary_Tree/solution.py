# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        v = root.val
        q = [root]
        i = 0
        while i < len(q):
            n = q[i]
            i += 1
            children = [n.left, n.right]
            for c in children:
                if c is not None:
                    if c.val != v:
                        return False
                    q.append(c)
        return True
