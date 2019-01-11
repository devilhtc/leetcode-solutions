# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def jsonfy(node):
            if node is None:
                return None
            return {"v": node.val, "l": jsonfy(node.left), "r": jsonfy(node.right)}

        return json.dumps(jsonfy(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def dejsonfy(o):
            if o == None:
                return None
            node = TreeNode(int(o["v"]))
            node.left = dejsonfy(o["l"])
            node.right = dejsonfy(o["r"])
            return node

        return dejsonfy(json.loads(data))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
