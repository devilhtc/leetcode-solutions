# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def smallestFromLeaf(self, root: "TreeNode") -> "str":
        stack = []
        self.out = None
        self.dfs(root, stack)
        return self.out

    def dfs(self, node, stack):
        if node is None:
            return
        c = chr(ord("a") + node.val)
        stack.append(c)
        if node.left is None and node.right is None:
            if self.out is None:
                self.out = "".join(reversed(stack))
            else:
                s = "".join(reversed(stack))
                if s < self.out:
                    self.out = s
        self.dfs(node.left, stack)
        self.dfs(node.right, stack)
        stack.pop()
