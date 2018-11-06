# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inorder = inorder
        self.postorder = postorder
        self.di = {v: i for i, v in enumerate(inorder)}
        self.dp = {v: i for i, v in enumerate(postorder)}
        l = len(inorder)
        return self.helper(0, l - 1, 0, l - 1)

    def helper(self, si, ei, sp, ep):
        if si > ei:
            return None
        elif si == ei:
            return TreeNode(self.inorder[si])
        cur = self.postorder[ep]
        node = TreeNode(cur)
        lsize = self.di[cur] - si
        rsize = ei - si - lsize
        node.left = self.helper(si, si + lsize - 1, sp, sp + lsize - 1)
        node.right = self.helper(ei - rsize + 1, ei, ep - rsize, ep - 1)
        return node
