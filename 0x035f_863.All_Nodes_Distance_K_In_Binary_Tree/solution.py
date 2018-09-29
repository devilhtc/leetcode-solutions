# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if K == 0:
            return [target.val]
        self.g = collections.defaultdict(list)
        self.buildg(root, None)
        self.v = set()
        self.out = []
        self.bfs(target.val, K)
        return self.out

    def bfs(self, cur, s):
        if cur in self.v:
            return
        self.v.add(cur)
        if s == 0:
            self.out.append(cur)
            return
        for c in self.g[cur]:
            self.bfs(c, s - 1)

    def buildg(self, node, pv):
        if node is None:
            return
        if pv is not None:
            self.g[pv].append(node.val)
            self.g[node.val].append(pv)
        self.buildg(node.left, node.val)
        self.buildg(node.right, node.val)
