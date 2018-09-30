class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        A2 = [(collections.Counter(ele), ele) for ele in A]
        criterion = collections.defaultdict(int)
        for ele in B:
            ctr = collections.Counter(ele)
            for k in ctr:
                criterion[k] = max(criterion[k], ctr[k])
        return [o for a, o in A2 if all(criterion[k] <= a.get(k, 0) for k in criterion)]
