class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        if len(arr) <= 1:
            return len(arr)
        
        maxtil = [arr[0]]
        minup = [arr[-1]]

        for i in range(len(arr) - 2):
            maxtil.append(max(maxtil[-1], arr[i+1]))
            minup.append(min(minup[-1], arr[-1*(i+2)]))
        minup = minup[::-1]

        chunks = 1 + sum(1 for a, b in zip(maxtil, minup) if a <= b)
        
        return chunks