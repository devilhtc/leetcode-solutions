# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minDis = 0
        if root.left is not None:
            minDis = abs(root.val - root.left.val)
        if root.right is not None:
            minDis = abs(root.val - root.right.val)
        self.minDis = minDis
        self.postOrder(root)
        return self.minDis
    
    def postOrder(self, node):
        minVal = node.val
        maxVal = node.val
        if node.left is not None:
            leftMinVal, leftMaxVal = self.postOrder(node.left)
            self.minDis = min(node.val - leftMaxVal, self.minDis)
            minVal = leftMinVal
        if node.right is not None:
            rightMinVal, rightMaxVal = self.postOrder(node.right)
            self.minDis = min(rightMinVal - node.val, self.minDis)
            maxVal = rightMaxVal
        return minVal, maxVal
        
        