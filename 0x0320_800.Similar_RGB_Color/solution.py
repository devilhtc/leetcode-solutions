class Solution:
    def similarRGB(self, color: "str") -> "str":
        def closest(s):
            snum = int(s, 16)
            x = snum % 17
            if x < 17 - x:
                o = snum - x
            else:
                o = snum + 17 - x
            o = "{0:2x}".format(o).replace(" ", "0")
            return o

        out = ["#"]
        for i in range(3):
            out.append(closest(color[i * 2 + 1 : i * 2 + 3]))
        return "".join(out)
