class Solution:
    def buddyStrings(self, A: "str", B: "str") -> "bool":
        if len(A) != len(B):
            return False
        diffs = []
        s = set([])
        has_dup = False
        for i in range(len(A)):
            if A[i] != B[i]:
                diffs.append(i)
                if len(diffs) == 2:
                    j, k = diffs
                    if A[j] != B[k] or A[k] != B[j]:
                        return False
                    for p in range(i + 1, len(A)):
                        if A[p] != B[p]:
                            return False
                    return True
            else:
                if has_dup:
                    continue
                if A[i] in s:
                    has_dup = True
                s.add(A[i])
        if len(diffs) == 0 and has_dup:
            return True
        return False
