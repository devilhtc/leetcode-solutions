"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Codec:
    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        
        :type root: Node
        :rtype: TreeNode
        """
        if root is None:
            return None
        children = [self.encode(c) for c in root.children]
        if len(children) == 0:
            return TreeNode(root.val)
        left = None
        for c in children:
            a = TreeNode(root.val)
            a.right = c
            a.left = left
            left = a
        return left

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        
        :type data: TreeNode
        :rtype: Node
        """
        if data is None:
            return None
        children = []
        cur = data
        while cur:
            c = self.decode(cur.right)
            if c:
                children.append(c)
            cur = cur.left
        node = Node(data.val, list(reversed(children)))
        return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
