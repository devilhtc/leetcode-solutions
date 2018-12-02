# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        d1 = {}
        d2 = {}
        self.encode(root1, d1)
        self.encode(root2, d2)
        return d1 == d2
    
    def encode(self, node, d):
        if node is None:
            return ''
        d[node.val] = ','.join(
            sorted([
                self.encode(node.left, d),
                self.encode(node.right, d)
            ])
        )
        return str(node.val)
        
        