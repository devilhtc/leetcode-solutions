class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        return len(set([self.gensig(e) for e in emails]))

    def gensig(self, e):
        l, r = tuple(e.split("@"))
        if "+" in l:
            l = l[: l.find("+")]
        l = l.replace(".", "")
        return l + "@" + r
