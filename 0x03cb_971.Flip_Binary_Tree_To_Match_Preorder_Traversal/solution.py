# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        if root is None:
            return []
        self.tree = collections.defaultdict(list)
        self.ct(root)
        self.flip = []
        v2idx = {v: i for i, v in enumerate(voyage)}

        for i, v in enumerate(voyage):
            children = self.tree[v]
            if len(children) == 2:
                li = v2idx.get(children[0], -1)
                ri = v2idx.get(children[1], -1)
                if li == -1 or ri == -1:
                    return [-1]
                if li > ri:
                    self.flip.append(v)

        self.preorder = []
        self.traverse(root)
        if len(self.preorder) == len(voyage) and all(
            self.preorder[i] == voyage[i] for i in range(len(voyage))
        ):
            return self.flip
        return [-1]

    def ct(self, node):
        if node is None:
            return
        if node.left is not None:
            self.tree[node.val].append(node.left.val)
            self.ct(node.left)
        if node.right is not None:
            self.tree[node.val].append(node.right.val)
            self.ct(node.right)

    def traverse(self, node):
        if node is None:
            return
        self.preorder.append(node.val)
        for c in (
            [node.right, node.left]
            if node.val in self.flip
            else [node.left, node.right]
        ):
            self.traverse(c)
