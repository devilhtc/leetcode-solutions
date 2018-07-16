class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        lcp = []
        minlen = min([len(ele) for ele in strs])
        for i in range(minlen):
            cur = strs[0][i]
            for s in strs:
                if s[i] != cur:
                    return "".join(lcp)
            lcp.append(cur)
        return "".join(lcp)
