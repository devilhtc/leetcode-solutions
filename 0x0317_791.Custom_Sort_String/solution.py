class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        S_dict = {S[i]: i  for i in range(len(S))}
        def cmp_char(a, b):
            return S_dict.get(a, len(S)) - S_dict.get(b, len(S))
        return ''.join(sorted(list(T), cmp = cmp_char))
        