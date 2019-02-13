import unittest
import random


class Solution:
    def search(self, nums: "List[int]", target: "int") -> "bool":
        def helper(lo, hi):
            if lo == hi:
                return nums[lo] == target
            if lo < hi:
                mi = (lo + hi) // 2
                if nums[mi] == target:  # found!
                    return True
                elif nums[mi] == nums[lo] == nums[hi]:  # cant tell
                    if helper(lo + 1, mi - 1):
                        return True
                    return helper(mi + 1, hi - 1)
                elif nums[hi] > nums[lo]:  # sorted already
                    if target < nums[lo] or target > nums[hi]:
                        return False
                    elif target < nums[mi]:
                        return helper(lo, mi - 1)
                    else:
                        return helper(mi + 1, hi)
                else:
                    if nums[mi] >= nums[lo]:  # left part sorted
                        if nums[lo] <= target < nums[mi]:
                            return helper(lo, mi - 1)
                        else:
                            return helper(mi + 1, hi)
                    else:
                        if nums[hi] >= target >= nums[mi]:
                            return helper(mi + 1, hi)
                        else:
                            return helper(lo, mi - 1)
            return False

        return helper(0, len(nums) - 1)


class TestSIRA2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.int_range = [-10, 50]
        self.basic_testcases = [
            (([1, 2, 3], 2), True),
            (([2, 2, 2, 2, 3, 2, 2], 3), True),
            (([2, 3, 4, 5, -1, -1, 0, 0, 0, 0, 0, 1, 2, 2], 1), True),
            (([2, 3, 4, 5, 6, 7, 12, -2, 2], 1), False),
        ]
        self.random_testcases = [
            self.generate_test_case(random.randint(2, 1000)) for _ in range(20)
        ] + [
            self.generate_test_case(random.randint(2, 1000), force_true=True)
            for _ in range(20)
        ]

    def test_basic(self):
        for inputs, output in self.basic_testcases:
            self.assertEqual(self.solution.search(*inputs), output)

    def test_random(self):
        for inputs, output in self.random_testcases:
            self.assertEqual(self.solution.search(*inputs), output)

    def generate_test_case(self, size: "int", force_true=False) -> "tuple":
        arr = [random.randint(*self.int_range) for _ in range(size)]
        tar = random.choice(arr) if force_true else random.randint(*self.int_range)
        arr = sorted(arr)
        p = random.randint(0, size - 1)
        arr = arr[p:] + arr[:p]
        return ((arr, tar), tar in arr)


if __name__ == "__main__":
    unittest.main()
