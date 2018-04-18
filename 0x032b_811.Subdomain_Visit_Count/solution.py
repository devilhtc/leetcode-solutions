class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        def getCountAndDomain(cpdomain):
            splitted = cpdomain.split(' ')
            return int(splitted[0]), splitted[1] 
            
        def getSubdomains(domain):
            domains = [d for d in domain.split('.')]
            domains.reverse()
            curd = domains[0]
            out = [curd]
            for i in range(1, len(domains)):
                curd = domains[i] + '.' + curd
                out.append(curd)
            return out
        
        d = {}
        for cpdomain in cpdomains:
            count, domain = getCountAndDomain(cpdomain)
            subdomains = getSubdomains(domain)
            for s in subdomains:
                d[s] = d.get(s, 0) + count
        return [str(d[k]) + ' ' + k for k in d]
        
    
    
            
        