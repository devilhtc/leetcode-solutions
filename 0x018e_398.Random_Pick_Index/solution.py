class Solution:
    def __init__(self, nums: "List[int]"):
        self.si = {}  # start index
        self.ei = {}
        self.c = {}
        self.nums = nums
        for i, v in enumerate(nums):
            if v not in self.si:
                self.si[v] = i
            self.ei[v] = i
            if v not in self.c:
                self.c[v] = 0
            self.c[v] += 1

    def pick(self, target: "int") -> "int":
        v = target
        if v not in self.c:
            return -1
        r = self.c[v]
        i = self.si[v]
        while r > 1:
            if self.nums[i] != v:
                i += 1
            else:
                a = random.random()
                if a < 1 / r:
                    return i
                else:
                    r -= 1
                    i += 1
        return self.ei[v]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
