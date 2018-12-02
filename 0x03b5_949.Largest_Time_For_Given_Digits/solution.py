class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        partitions = []
        
        for i in range(4):
            for j in range(i + 1, 4):
                partitions.append(
                    (
                        [A[i], A[j]],
                        [A[k] for k in range(4) if k != i and k != j]
                    ),
                )
        
        candidates = [(-1, '')]
        for hrs, mins in partitions:
            for i in range(2):
                for j in range(2):
                    h = hrs[i] * 10 + hrs[1 - i]
                    m = mins[j] * 10 + mins[1 - j]
                    if 24 > h >= 0 and 60 > m >= 0:
                        candidates.append(
                            (
                                h * 60 + m, 
                                str(hrs[i]) + str(hrs[1 - i]) + ':' + str(mins[j]) + str(mins[1 - j])
                            )
                        )
        return max(candidates)[1]
            