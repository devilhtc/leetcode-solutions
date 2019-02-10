class Solution:
    def equationsPossible(self, equations: "List[str]") -> "bool":

        # union-find
        uf = {}

        def union(i, j):
            fi = find(i)
            fj = find(j)
            if fi == fj:
                return
            if fj < fi:
                fj, fi = fi, fj
            uf[fj] = fi

        def find(i):
            if i not in uf:
                uf[i] = i
                return i
            f = uf[i]
            while uf[f] != f:
                f = uf[f]
            uf[i] = f
            return f

        # convert a character to a number
        def char2num(c):
            return ord(c) - ord("a")

        # union the equalities
        for eq in equations:
            if eq[1:3] == "==":
                union(char2num(eq[0]), char2num(eq[3]))

        # find out if there is any inconsistency
        # which can only happen if two numbers that should be equal are not
        for eq in equations:
            if eq[1:3] == "!=":
                if find(char2num(eq[0])) == find(char2num(eq[3])):
                    return False

        return True
