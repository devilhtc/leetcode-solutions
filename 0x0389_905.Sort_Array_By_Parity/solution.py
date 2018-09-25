class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        e, o = [], []
        for ele in A:
            if ele % 2 == 0:
                e.append(ele)
            else:
                o.append(ele)
        return e + o
        