# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    def bstFromPreorder(self, preorder: "List[int]") -> "TreeNode":
        stack = []
        rs = {}
        prev = None
        for i, v in enumerate(preorder):
            j = None
            while len(stack) > 0 and stack[-1][0] < v:
                prev, j = stack.pop()
            if j is not None:
                rs[j] = i
            stack.append((v, i))

        def helper(s, e):
            if s == e:
                return TreeNode(preorder[s])
            elif s > e:
                return None
            node = TreeNode(preorder[s])
            le = e
            if s in rs:
                node.right = helper(rs[s], e)
                le = rs[s] - 1
            node.left = helper(s + 1, le)
            return node

        return helper(0, len(preorder) - 1)

    def bstToPreorder(self, node):
        cur, out = None, []

        def preorder(node):
            if not node:
                return
            out.append(node.val)
            for c in [node.left, node.right]:
                preorder(c)

        return out


"""
if __name__ == '__main__':
    # few testcases
    s = Solution()
    cases = [
        [8,5,1,7,10,12],
        [2,1,3],
        [1,3,2],
        [1,2,3,4,5],
        [5,4,3,2,1],
        [1,3,5,9,7],
        [1,10,2,9,3,8,4,7,5,6],
        [1,10,2,11],
        []
    ]
    for po in cases:
        print(po)
        o = s.bstFromPreorder(po)
        po2 = s.bstToPreorder(o)
        assert all(a == b for a, b in zip(po, po2)), 'case {} failed'.format(po)
"""
