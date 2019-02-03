# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def verticalTraversal(self, root: "TreeNode") -> "List[List[int]]":
        self.d = {}
        self.dfs(root, 0, 0)
        out = []
        for k in sorted(list(self.d.keys())):
            cur = []
            d2 = self.d[k]
            for k2 in sorted(list(d2.keys()), reverse=True):
                for ele in sorted(d2[k2]):
                    cur.append(ele)
            out.append(cur)
        return out

    def dfs(self, node, x, y):
        if node is None:
            return
        if x not in self.d:
            self.d[x] = {}
        d2 = self.d[x]
        if y not in d2:
            d2[y] = [node.val]
        else:
            d2[y].append(node.val)
        self.dfs(node.left, x - 1, y - 1)
        self.dfs(node.right, x + 1, y - 1)
