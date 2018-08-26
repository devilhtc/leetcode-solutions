# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        self.pre = pre
        self.post = post
        self.post_dict = {post[i]: i for i in range(len(post))}
        return self.constructHelper(0, len(pre) - 1, 0)

    def constructHelper(self, s1, e1, s2):
        e2 = e1 - s1 + s2
        if s1 > e1:
            return None
        cur = TreeNode(self.pre[s1])
        if e1 > s1:
            left_val = self.pre[s1 + 1]
            left_post_end = self.post_dict[left_val]
            left_tree_size = left_post_end - s2 + 1
            right_tree_size = e1 - s1 - left_tree_size
            cur.left = self.constructHelper(s1 + 1, s1 + left_tree_size, s2)
            cur.right = self.constructHelper(
                s1 + left_tree_size + 1, e1, e2 - right_tree_size
            )
        return cur
