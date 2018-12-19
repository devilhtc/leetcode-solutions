# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        self.roots = [None, None]
        self.cps = [None, None]
        self.V = V
        self.helper(root)
        return self.roots

    def helper(self, node):
        if node is None:
            return
        i = 0 if node.val <= self.V else 1

        if self.roots[i] is None:
            self.roots[i] = node
        else:
            if node.val < self.cps[i].val:
                self.cps[i].left = node
            else:
                self.cps[i].right = node
        self.cps[i] = node

        # if leq, no need to check left
        if i == 0:
            c = node.right
            node.right = None
        else:
            c = node.left
            node.left = None
        self.cps[i] = node
        self.helper(c)
