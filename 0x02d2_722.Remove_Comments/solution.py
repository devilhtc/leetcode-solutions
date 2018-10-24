class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """

        ns = "\n".join(source)
        b1 = False  # for //
        b2 = False  # for /* ... */
        outlist = (
            []
        )  # collect characters in a string to avoid re-write strings (which are immutable)
        i = 0

        while i < len(ns):  # use a while loop so that we can skip characters
            c2 = ns[i : i + 2]
            c = ns[i]
            if b2:  # in /*
                if c2 == "*/":
                    b2 = False
                    i += 1
            elif b1:  # in //
                if c == "\n":
                    outlist.append(c)
                    b1 = False
            else:  # not in comment section, determine if in comment section, if not add the character
                if c2 == "//":
                    b1 = True
                    i += 1
                elif c2 == "/*":
                    b2 = True
                    i += 1
                else:
                    outlist.append(c)
            i += 1

        outStr = "".join(outlist)
        out = [
            line for line in outStr.split("\n") if line != ""
        ]  # filter out the empty lines

        return out
