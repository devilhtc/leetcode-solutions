class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        def pour(prev):
            out = [0.0] * (len(prev) + 1)
            for i in range(len(prev)):
                spill = max(0.0, (prev[i] - 1.0)/2.0)
                out[i] += spill
                out[i + 1] += spill
            return out
        row = [poured]
        for _ in range(query_row):
            row = pour(row)
        return min(row[query_glass], 1.0)
        