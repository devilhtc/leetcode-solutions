class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """

        def gen_sig(s):
            out = []
            if len(s) == 0:
                return out
            ch = s[0]
            co = 0
            for i, v in enumerate(s):
                if v == ch:
                    co += 1
                else:
                    out.append((ch, co))
                    ch = v
                    co = 1
            out.append((ch, co))
            return out

        sig_name = gen_sig(name)
        sig_typed = gen_sig(typed)
        return len(sig_name) == len(sig_typed) and all(
            sig_name[i][0] == sig_typed[i][0] and sig_name[i][1] <= sig_typed[i][1]
            for i in range(len(sig_name))
        )
