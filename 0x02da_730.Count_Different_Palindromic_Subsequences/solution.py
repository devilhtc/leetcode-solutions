class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        ORDER = "abcd"
        MOD = 1000000007
        c2idx = {c: i for i, c in enumerate(ORDER)}

        pre_idx = []
        cur_idx = [-1] * 4
        for i, c in enumerate(S):
            idx = c2idx[c]
            cur_idx[idx] = max(cur_idx[idx], i)
            pre_idx.append(list(cur_idx))

        next_idx = []
        cur_idx = [len(S)] * 4
        for i in range(len(S) - 1, -1, -1):
            c = S[i]
            idx = c2idx[c]
            cur_idx[idx] = min(cur_idx[idx], i)
            next_idx.append(list(cur_idx))
        next_idx = list(reversed(next_idx))

        memo = {}

        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            out = 0
            for c in "abcd":
                idx = c2idx[c]
                ni, pi = next_idx[i][idx], pre_idx[j][idx]
                if ni <= j and pi >= i:
                    out = (out + (1 if ni == pi else (2 + dp(ni + 1, pi - 1)))) % MOD
            memo[(i, j)] = out
            return out

        return dp(0, len(S) - 1)
