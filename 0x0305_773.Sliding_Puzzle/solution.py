start = [1, 2, 3, 4, 5, 0]
minstep = {tuple(start): 0}
q = collections.deque([(start, 0)])
next_pos = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [3, 5, 1], 5: [2, 4]}


def get_children(s):
    zpos = [i for i, v in enumerate(s) if v == 0][0]
    out = []
    for npos in next_pos[zpos]:
        s[npos], s[zpos] = s[zpos], s[npos]
        out.append(list(s))
        s[npos], s[zpos] = s[zpos], s[npos]
    return out


while len(q) > 0:
    a, i = q.popleft()
    for c in get_children(a):
        csig = tuple(c)
        if csig in minstep:
            continue
        else:
            minstep[csig] = i + 1
            q.append((c, i + 1))


class Solution:
    def slidingPuzzle(self, board: "List[List[int]]") -> "int":
        return minstep.get(tuple(board[0] + board[1]), -1)
