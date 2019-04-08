# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        path = []
        out = [0]

        def dfs(node):
            if node is None:
                return
            path.append(node.val)
            if node.left is None and node.right is None:
                s = 0
                l = len(path)
                base = 1
                for i in range(l):
                    s += base * path[l - 1 - i]
                    base = base * 2
                out[0] += s
            dfs(node.left)
            dfs(node.right)
            path.pop()

        dfs(root)
        return out[0]
