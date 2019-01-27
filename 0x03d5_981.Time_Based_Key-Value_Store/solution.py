class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(list)

    def set(self, key: "str", value: "str", timestamp: "int") -> "None":
        self.d[key].append((timestamp, value))

    def get(self, key: "str", timestamp: "int") -> "str":
        if len(self.d[key]) == 0:
            return ""
        arr = self.d[key]
        if arr[0][0] > timestamp:
            return ""
        lo, hi = 0, len(arr) - 1
        while hi > lo + 1:
            mi = (hi + lo) // 2
            if arr[mi][0] > timestamp:
                hi = mi - 1
            else:
                lo = mi
        if arr[hi][0] <= timestamp:
            return arr[hi][1]
        return arr[lo][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
