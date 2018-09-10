
"""
Python PriorityQueue that supports
push, pop and most importantly >>> remove <<<

author: devilhtc
"""
from collections import deque
import unittest


class PriorityQueue:
    """
    My own damn PriorityQueue
    uses a heap to keep track of values
    and a dequeue to keep track of boundary
    """

    class _HNode:
        """
        heap node for storing items
        if a node has item None, it is a boundary node
        """

        def __init__(self, item, cmp=None):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None

        def heapfloat(self):
            pass

        def heapsink(self):
            pass

    def __init__(self, cmp=None):
        """
        Constructor of priority heap
        Kwargs:
            cmp: a function that compares two items    
        """
        self._cmp = cmp
        self._build()

    # public api

    def push(self, item):
        pass

    def pop(self):
        pass

    def remove(self, item):
        pass

    # helper functions

    def _hnode(self, item=None):
        return self._HNode(item, cmp=self._cmp)

    def _build(self):
        self._head = self._hnode()
        self._size = 0
        self._itemid2node = {}
        self._boundaryhead = deque([self._head])

    def _gennext(self):
        out = self._boundaryhead
        if self._size == 0:
            pass
        return out

    def _removelast(self):
        pass


class PriorityQueueTestCases(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(1, 2 - 1)


if __name__ == "__main__":
    unittest.main()
