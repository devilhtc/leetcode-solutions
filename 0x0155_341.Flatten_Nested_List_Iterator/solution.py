# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        if len(nestedList) == 0:
            self.stack = []
        self.stack = [[nestedList, 0]]
        self._findNext()

    def next(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            raise Exception("wtf")
        a, b = self.stack[-1]
        out = a[b].getInteger()
        self.stack[-1][1] += 1
        self._findNext()
        return out

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def _findNext(self):
        while len(self.stack) > 0:
            a, b = self.stack[-1]
            if b == len(a):
                self.stack.pop()
                if len(self.stack) > 0:
                    self.stack[-1][1] += 1
                continue
            else:
                if a[b].isInteger():
                    break
                else:
                    a2 = a[b].getList()
                    self.stack.append([a2, 0])


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
