from functools import lru_cache


class Solution:
    def numSquarefulPerms(self, A: "List[int]") -> "int":
        l = len(A)
        out = [0]
        c = dict(collections.Counter(A))  # element - counts
        s = []  # stack

        @lru_cache(maxsize=None)
        def is_square(s):
            return int(math.sqrt(s)) ** 2 == s

        def dfs(stack, counts):
            if len(stack) == l:
                out[0] += 1
                return
            # keep track of options to avoid duplicate steps
            options = [k for k, v in counts.items() if v > 0]
            for o in options:
                # can take a step if the stack is empty
                # or the tip of the stack + option is square
                if len(stack) == 0 or is_square(stack[-1] + o):
                    # dfs + backtrack
                    counts[o] -= 1
                    stack.append(o)
                    dfs(stack, counts)
                    stack.pop()
                    counts[o] += 1

        dfs(s, c)
        return out[0]
