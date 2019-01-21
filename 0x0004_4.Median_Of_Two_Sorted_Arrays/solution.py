class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0 and len(nums2) == 0:
            return None

        def med(arr):
            if len(arr) % 2 == 1:
                return arr[len(arr) // 2]
            else:
                return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2

        if len(nums1) == 0:
            return med(nums2)
        if len(nums2) == 0:
            return med(nums1)

        if len(nums1) < len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        # now nums1 is the longer one
        total_length = len(nums1) + len(nums2)
        k = total_length // 2
        lo = k - len(nums2)
        hi = k
        out = None
        while hi >= lo:
            mi = (hi + lo) // 2
            l1, r1 = (
                float("-inf") if mi == 0 else nums1[mi - 1],
                float("inf") if (mi == k and len(nums1) == k) else nums1[mi],
            )
            len_rest = k - mi
            l2, r2 = (
                float("-inf") if len_rest == 0 else nums2[len_rest - 1],
                float("inf") if len_rest == len(nums2) else nums2[len_rest],
            )
            if l1 <= r2 and l2 <= r1 or lo == hi:
                out = (
                    min(r1, r2)
                    if total_length % 2 == 1
                    else (max(l1, l2) + min(r1, r2)) / 2
                )
                break
            elif l1 >= r2:
                hi = mi - 1
            else:
                lo = mi + 1

        return out
