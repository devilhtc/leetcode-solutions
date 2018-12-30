# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        _, v2, v3 = self.helper(root)
        return v3 if v2 < 0 else min(v2, v3)

    def helper(self, node):
        if node is None:
            return -1, 0, -1

        l1, l2, l3 = self.helper(node.left)
        r1, r2, r3 = self.helper(node.right)

        c1 = l2 + r2 if (l2 >= 0 and r2 >= 0) else -1
        c2 = (
            min([l3 + r3, (l3 if l2 < 0 else l2) + r3, (r3 if r2 < 0 else r2) + l3])
            if (l3 > 0 and r3 > 0)
            else max(l3, r3)
        )
        c3 = (
            1
            + min([ele for ele in [l1, l2, l3] if ele >= 0])
            + min([ele for ele in [r1, r2, r3] if ele >= 0])
        )
        return c1, c2, c3
