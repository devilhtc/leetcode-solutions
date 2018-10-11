# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class CBTInserter:
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = {}
        q = [root]
        i = 0
        # bfs to keep track
        while i < len(q):
            cur = q[i]
            if cur is not None:
                self.nodes[i] = cur
                i += 1
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
        self.c = i

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        cur = TreeNode(v)
        self.nodes[self.c] = cur
        # use the counter to find parent
        parent = self.nodes[(self.c - 1) // 2]
        if self.c % 2 == 1:
            parent.left = cur
        else:
            parent.right = cur
        self.c = self.c + 1
        return parent.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.nodes.get(0, None)


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
