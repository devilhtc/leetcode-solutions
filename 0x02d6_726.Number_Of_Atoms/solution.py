def getNextElemAndCount(s, start, d):
    k = start
    while k<len(s):
        i = k
        if i >= len(s):
            return 
        elem = s[i]
        ns = i+1
        if i<len(s)-1 and not s[i+1].isdigit() and s[i+1] == s[i+1].lower():
            elem = s[i:i+2]
            ns = i+2
        j = ns
        while j<len(s) and s[j].isdigit():
            j+=1
        count = 1
        if j > ns:
            count = int(s[ns:j])
        d[elem] = d.get(elem, 0) + count
        k = j
        
def findClosing(s, i):
    count = 1
    for j in range(i, len(s)):
        if s[j] == '(':
            count+=1
        if s[j] == ')':
            count-=1
        if count == 0:
            return j
    return j
    
class Solution(object):
    def countOfAtoms(self, formula):
        d = self.countOfAtomsHelper(formula)
        keys = [k for k in d]
        keys = sorted(keys)
        out = []
        for k in keys:
            out.append(k)
            if d[k]>1:
                out.append(str(d[k]))
        return ''.join(out)
        
    def countOfAtomsHelper(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        #print formula
        if '(' in formula:
            s = formula.find('(')
            e = findClosing(formula, s+1)
            inner = formula[s+1:e]
            dinner = self.countOfAtomsHelper(inner)
            digits = ''
            i = e+1
            while (i<len(formula) and formula[i].isdigit()):
                digits += formula[i]
                i+=1
            count = int(digits)
            
            outer = formula[:s] + formula[e+1+len(digits):]
            douter = self.countOfAtomsHelper(outer)
            
            for k in dinner:
                douter[k] = douter.get(k, 0) + count * dinner[k]
            return douter   
        else:
            d = {}
            getNextElemAndCount(formula, 0, d)
            return d
        
        
        