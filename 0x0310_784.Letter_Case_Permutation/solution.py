class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        str_idx = set([i for i in range(len(S)) if not S[i].isdigit()])
        out = []
        stack = []
        def dfs(i, cur_stack):
            if i == len(S):
                out.append(''.join(cur_stack))
                return 
            if i in str_idx:
                cur_stack.append(S[i].lower())
                dfs(i+1, cur_stack)
                cur_stack.pop()
                cur_stack.append(S[i].upper())
                dfs(i+1, cur_stack)
                cur_stack.pop()
            else:
                cur_stack.append(S[i])
                dfs(i+1, cur_stack)
                cur_stack.pop()
        dfs(0, stack)
        return out
        