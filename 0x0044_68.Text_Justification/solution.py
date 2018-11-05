class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        def patch_lines(line):
            num_spaces = len(line) - 1
            if num_spaces == 0:
                return line[0] + " " * (maxWidth - len(line[0]))
            len_spaces = maxWidth - sum(len(w) for w in line)
            base = len_spaces // num_spaces
            longer_count = len_spaces % num_spaces
            out = []
            for i, w in enumerate(line):
                out.append(w)
                if i < len(line) - 1:
                    out.append(" " * (base + (1 if i < longer_count else 0)))
            return "".join(out)

        lines = [[]]
        a = b = 0  # a: word length, b: word count
        for w in words:
            if a + b + len(w) <= maxWidth:
                lines[-1].append(w)
                a += len(w)
                b += 1
            else:
                lines.append([w])
                a = len(w)
                b = 1

        out = []
        for i, line in enumerate(lines):
            if i < len(lines) - 1:
                out.append(patch_lines(line))
            else:
                l = " ".join(line)
                out.append(l + " " * (maxWidth - len(l)))
        return out
