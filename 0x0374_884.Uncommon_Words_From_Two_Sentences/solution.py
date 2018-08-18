class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        return (lambda x: [ele for ele in x if x[ele] == 1])(
            collections.Counter((A + " " + B).split())
        )
