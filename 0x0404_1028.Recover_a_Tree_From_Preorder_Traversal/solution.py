# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def get_next(i):
            # returns (val, depth, next_idx) tuple
            # next_idx = len(S) means ends
            d = 0
            v = 0
            while i < len(S):
                if S[i] == "-":
                    d += 1
                    i += 1
                    continue
                fi = (i == len(S) - 1) or (S[i + 1] == "-")
                v = v * 10 + int(S[i])
                i += 1
                if fi:
                    break
            return d, v, i

        stack = []
        i = 0
        pd = -1
        root = None
        while i < len(S):
            d, v, i = get_next(i)
            node = TreeNode(v)
            if root is None:
                root = node
            if d == pd + 1:
                if len(stack) > 0:
                    stack[-1][0].left = node
            else:
                while len(stack) > 0:
                    node2, d2 = stack.pop()
                    if d == d2 + 1:
                        node2.right = node
                        break
            stack.append((node, d))
            pd = d
        return root
