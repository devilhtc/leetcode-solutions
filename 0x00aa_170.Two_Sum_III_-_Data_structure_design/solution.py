class TwoSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.sums = set()

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number not in self.d:
            self.d[number] = 0
        self.d[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        self._find_helper(value)
        return value in self.sums

    def _find_helper(self, value):
        if value in self.sums:
            return
        if value % 2 == 0 and self.d.get(value // 2, 0) >= 2:
            self.sums.add(value)
            return
        p = None
        for k, v in self.d.items():
            # try to find the complement
            if self.d.get(value - k, 0) - (k * 2 == value) > 0:
                self.sums.add(value)
                return
            # cache contiguous sums
            if p != None:
                self.sums.add(k + p)
            # cache duplicate element sums
            if v >= 2:
                self.sums.add(2 * k)
            p = k


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
