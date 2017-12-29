class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        out = []
        toName = {}
        visited = {}
        d = {}
        for account in accounts:
            name = account[0]
            if len(account) > 1:
                priE = account[1]
                toName[priE] = name
                if priE not in d:
                    d[priE] = []
                for e in account[2:]:
                    if e not in d:
                        d[e] = []
                    d[e].append(priE)
                    d[priE].append(e)
                for e in account[1:]:
                    if e not in visited:
                        visited[e] = False
            else:
                out.append([name])
        
        for e in visited:
            o = []
            self.dfs(d, visited, e, o)
            if len(o)>0:
                name = None
                for e2 in o:
                    if name is None:
                        if e2 in toName:
                            name = toName[e2]
                out.append([name] + sorted(o))
        return out
    
        
    def dfs(self, d, visited, cur, o):
        if visited[cur]: return
        
        visited[cur] = True
        o.append(cur)
        for child in d[cur]:
            self.dfs(d, visited, child, o)
        
        
                    

        