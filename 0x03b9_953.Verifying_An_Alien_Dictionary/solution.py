class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_dict = {c: i for i, c in enumerate(order)}

        def leq(a, b):
            if b.startswith(a):
                return True
            for i in range(min(len(a), len(b))):
                oa = order_dict[a[i]]
                ob = order_dict[b[i]]
                if oa < ob:
                    return True
                elif oa > ob:
                    return False
            return False

        for i in range(len(words) - 1):
            if not leq(words[i], words[i + 1]):
                return False
        return True
