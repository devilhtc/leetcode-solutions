# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findLeaves(self, root: "TreeNode") -> "List[List[int]]":
        out = []

        def post_order(node):
            if node is None:
                return -1
            cur = max(post_order(node.left), post_order(node.right)) + 1
            if len(out) <= cur:
                out.append([])
            out[cur].append(node.val)
            return cur

        post_order(root)
        return out
