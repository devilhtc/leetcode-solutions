class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for r in A:
            self.processRow(r)

        return A

    def processRow(self, row):
        i = 0
        j = len(row) - 1
        while j > i:
            row[i], row[j] = 1 - row[j], 1 - row[i]
            j -= 1
            i += 1
        if i == j:
            row[i] = 1 - row[i]
