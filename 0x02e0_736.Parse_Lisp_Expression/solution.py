def isNumber(a):
    if a.startswith('-'):
        return True
    if a.isdigit():
        return True
    return False
    
def expression2arguments(expression):
    args = expression.split(' ')
    newArgs = []
    for a in args:
        if a.startswith('('):
            newArgs.append('(')
            newArgs.append(a[1:])
        elif a.endswith(')'):
            z = -1
            while a[z] == ')':    
                z -= 1
            newArgs.append(a[:z+1])
            for _ in range(- z - 1):
                newArgs.append(')')
        else:
            newArgs.append(a)
    return newArgs

def findParenthesis(args):
    stack = []
    par = {}
    for i in range(len(args)):
        if args[i] == '(':
            stack.append(i)
        elif args[i] == ')':
            par[stack.pop()] = i
    return par


class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        args = expression2arguments(expression)
        self.par = findParenthesis(args)
        #print args
        return self.helper(args, {}, 1, len(args) - 2)
        
    def getNextSetOfArgs(self, args, i, j):
        k = i
        out = []
        while k <= j:
            if k in self.par:
                out.append( (k+1, self.par[k] - 1) )
                k = self.par[k] + 1
            else:
                out.append( (k, k) )
                k += 1
        return out
                
    def helper(self, args, prevD, i, j):
        curD = dict(prevD)
        #print curD
        if j - i == 0:
            if isNumber(args[i]):
                return int(args[i])
            else:
                return curD[args[i]]
        allset = self.getNextSetOfArgs(args, i+1, j)
        print allset
        if args[i] == 'add' or args[i] == 'mult':
            fir = self.helper(args, curD, allset[0][0], allset[0][1])
            sec = self.helper(args, curD, allset[1][0], allset[1][1])
            if args[i] == 'add':
                return fir + sec
            else:
                return fir * sec
        # now it has to be let
        assert(args[i] == 'let', 'wait its not let')
        l = len(allset)
        for k in range(l/2):
            symbol = args[allset[2*k][0]]
            #print symbol
            value = self.helper(args, curD, allset[2*k + 1][0], allset[2*k + 1][1])
            curD[symbol] = value
        return self.helper(args, curD, allset[-1][0], allset[-1][1])
        