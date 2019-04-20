class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(s, e):
            if s >= e:
                return
            rd = nums[(s + e) // 2 + (s + e) % 2]
            lo, hi = [], []
            crd = 0
            for i in range(s, e + 1):
                if nums[i] == rd:
                    crd += 1
                elif nums[i] < rd:
                    lo.append(nums[i])
                else:
                    hi.append(nums[i])
            i = s
            for x in lo:
                nums[i] = x
                i += 1
            for _ in range(crd):
                nums[i] = rd
                i += 1
            for x in hi:
                nums[i] = x
                i += 1

            quicksort(s, s + len(lo) - 1)
            quicksort(e - len(hi) + 1, e)

        quicksort(0, len(nums) - 1)
        return nums
