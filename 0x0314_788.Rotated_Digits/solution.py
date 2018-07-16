# brute-force oneliner


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        return sum(
            [
                1
                for i in range(1, N + 1)
                if all(
                    [ele in ["1", "2", "5", "6", "8", "9", "0"] for ele in set(str(i))]
                )
                and any([ele in ["2", "5", "6", "9"] for ele in set(str(i))])
            ]
        )
