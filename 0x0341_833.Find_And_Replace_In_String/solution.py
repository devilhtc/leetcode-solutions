class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        if len(indexes) == 0:
            return S
        out = []
        z = sorted(list(zip(indexes, sources, targets)))
        out.append(S[: z[0][0]])

        for i, v in enumerate(z):
            idx, sou, tar = v
            m = True
            for j in range(len(sou)):
                if sou[j] != S[idx + j]:
                    m = False
                    break
            nidx = z[i + 1][0] if i < len(z) - 1 else len(S)
            if m:
                out.append(tar)
                out.append(S[idx + len(sou) : nidx])
            else:
                out.append(S[idx:nidx])

        return "".join(out)
