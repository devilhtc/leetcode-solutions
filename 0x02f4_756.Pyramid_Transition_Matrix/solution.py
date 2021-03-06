# now accepted solution (they decreased test size)


def getPyra(bottom):
    pyra = []
    for i in range(len(bottom) - 1):
        l = i + 1
        pyra.append(["." for _ in range(l)])
    pyra.append(list(bottom))
    return pyra


def getState(pyra, i, j):
    if j == 0:  # new row, just get the next row
        return "".join(pyra[i + 1])
    else:  # in the middle, get this row and next row ()
        return "".join(pyra[i]) + "," + "".join(["."] * j + pyra[i + 1][j:])


class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        self.d = {}
        for ele in allowed:
            key = (ele[0], ele[1])
            self.d[key] = self.d.get(key, []) + [ele[2]]
        self.memo = {}
        pyra = getPyra(bottom)
        return self.dp(pyra, len(bottom) - 2, 0)

    def dp(self, pyra, i, j):
        if i == 0 and j == 0:  # up to the top, just look for
            if (pyra[1][0], pyra[1][1]) in self.d:
                return True
            return False

        state = getState(pyra, i, j)
        # print pyra, state
        if state in self.memo:
            return self.memo[state]

        # next point
        ni = i - 1 if i == j else i
        nj = 0 if i == j else j + 1

        # determine what to put in i, j th point
        # if any returns true in subsequent call, cache and return
        ret = False
        key = (pyra[i + 1][j], pyra[i + 1][j + 1])
        possible = self.d.get(key, [])
        for char in possible:
            # if j > 0:
            #    if (pyra[i][j-1], char) not in self.d:
            #        continue
            pyra[i][j] = char
            if self.dp(pyra, ni, nj):
                ret = True
                break
        pyra[i][j] = "."
        self.memo[state] = ret
        # print pyra, ret
        return ret
