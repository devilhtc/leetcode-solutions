
"""
Python PriorityQueue that supports
push, pop and most importantly >>> remove <<<

author: devilhtc
"""
import unittest


class PriorityQueue:
    """
    My own damn PriorityQueue
    uses a heap (in the form a list) to keep track of values
    and a dictionary ()
    """

    debug = False

    def __init__(self, cmp=None):
        """
        Constructor of priority heap
        Kwargs:
            cmp: a function that compares two items    
        """
        self._cmpfunc = cmp
        self._heap = []
        self._tracker = {}  # item id - index in heap

    # public api

    def push(self, item):
        if item is None:
            raise ValueError("The item cannot be None")
        if id(item) in self._tracker:
            raise ValueError(
                "The item ({}) is already" " in the PriorityQueue".format(item)
            )
        self._heap.append(item)
        self._tracker[id(item)] = len(self._heap) - 1
        self._float(item)
        self._debug_log("push")

    def pop(self):
        if len(self._heap) == 0:
            raise IndexError("pop from empty PriorityQueue")
        out = self._heap[0]
        self.remove(out)
        self._debug_log("pop")
        return out

    def remove(self, item):
        if id(item) not in self._tracker:
            raise ValueError(
                "The item ({}) you wish to remove"
                "is not in the PriorityQueue".format(item)
            )

        last = self._heap[-1]

        self._swap(item, last)
        self._tracker.pop(id(item))
        self._heap.pop()

        if last is not item:
            self._sink(last)

    # helper functions

    def _sink(self, item):
        left, right = self._get_children(item)
        if self._cmp(item, left) <= 0 and self._cmp(item, right) <= 0:
            # item <= left, item <= right, no-op
            return
        elif self._cmp(item, left) >= 0 and self._cmp(item, right) <= 0:
            # left <= item <= right
            self._swap(item, left)
        elif self._cmp(item, left) <= 0 and self._cmp(item, right) >= 0:
            # right <= item <= left
            self._swap(item, right)
        # now left <= item, right <= item
        elif self._cmp(left, right) <= 0:
            # left <= right
            self._swap(item, left)
        else:
            # right <= left
            self._swap(item, right)
        self._sink(item)

    def _float(self, item):
        parent = self._get_parent(item)
        if parent is None:
            return
        if self._cmp(item, parent) <= 0:
            self._swap(item, parent)
            self._float(item)

    def _swap(self, item1, item2):
        if item1 is item2:
            return
        idx1, idx2 = self._tracker[id(item1)], self._tracker[id(item2)]
        self._heap[idx1], self._heap[idx2] = item2, item1
        self._tracker[id(item2)], self._tracker[id(item1)] = idx1, idx2

    def _get_children(self, item):
        idx = self._tracker[id(item)]
        return (self._get_node_by_idx(2 * idx + 1), self._get_node_by_idx(2 * idx + 2))

    def _get_parent(self, item):
        idx = self._tracker[id(item)]
        if idx == 0:
            return None
        return self._get_node_by_idx((idx - 1) // 2)

    def _get_node_by_idx(self, idx):
        return self._heap[idx] if 0 <= idx < len(self._heap) else None

    def _cmp(self, item1, item2):
        if item1 is None:
            return 1
        if item2 is None:
            return -1
        if self._cmpfunc is not None:
            return self._cmpfunc(item1, item2)
        if item1 == item2:
            return 0
        if item1 < item2:
            return -1
        else:
            return 1

    # debug only

    def _debug_log(self, after=None):
        if not self.debug:
            return
        if after is not None:
            print("after {}".format(after))
        print(self._heap)
        print({ele: self._tracker[id(ele)] for ele in self._heap})
        print()


class PriorityQueueTestCases(unittest.TestCase):
    def setUp(self):
        # test cases are arranged as
        # (operations, expected_return_values, constructor_args)
        self.basic_testcasts = [
            ([("push", [3]), ("pop", [])], [None, 3], None),
            (
                [
                    ("push", [5]),
                    ("push", [6]),
                    ("push", [7]),
                    ("push", [1]),
                    ("pop", []),
                    ("pop", []),
                    ("pop", []),
                    ("push", [8]),
                    ("push", [4]),
                    ("pop", []),
                    ("push", [11]),
                    ("push", [4]),
                    ("pop", []),
                    ("pop", []),
                ],
                [None, None, None, None, 1, 5, 6, None, None, 4, None, None, 4, 7],
                None,
            ),
            (
                [("push", [5]), ("push", [6]), ("remove", [5]), ("pop", [])],
                [None, None, None, 6],
                None,
            ),
        ]

    def test_basic(self):
        self._execute_test_cases(self.basic_testcasts)

    def test_errors(self):
        # pop from empty
        a = PriorityQueue()
        try:
            a.pop()
        except Exception as e:
            self.assertEqual(e.__class__, IndexError)

    def _execute_test_cases(self, cases):
        for ops, rets, cmpfunc in cases:
            pq = PriorityQueue(cmp=cmpfunc)
            for i in range(len(ops)):
                op = ops[i]
                expected_ret = rets[i]
                self.assertEqual(getattr(pq, op[0])(*op[1]), expected_ret)


if __name__ == "__main__":
    unittest.main()
