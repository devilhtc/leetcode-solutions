class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if len(tree) == 0:
            return 0
        f1 = tree[0]
        f2 = None
        c1 = 1
        c2 = 0
        i = 0
        j = 1
        out = 1
        while j < len(tree):
            cur = tree[j]
            if f1 is None or f2 is None or f1 == cur or f2 == cur:
                # can move j
                j += 1
                if f1 == cur:
                    c1 += 1
                elif f2 == cur:
                    c2 += 1
                elif f1 is None:
                    f1 = cur
                    c1 = 1
                else:
                    f2 = cur
                    c2 = 1
                out = max(c1 + c2, out)
            else:
                # cant move j, move i
                pre = tree[i]
                i += 1
                if pre == f1:
                    c1 -= 1
                    if c1 == 0:
                        f1 = None
                else:
                    c2 -= 1
                    if c2 == 0:
                        f2 = None
        return out
