class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h_max = [max(x) for x in grid]
        v_max = [max(x) for x in zip(*grid)]
        # *(a variable) = unpack the variable
        sum = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                sum = sum + min(h_max[r],v_max[c]) - val
                
        return sum