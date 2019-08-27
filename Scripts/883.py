class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top = 0
        max_h = [0] * len(grid)
        max_c = [0] * len(grid[0])

        for idx_r, row in enumerate(grid):
            for idx_c, cell in enumerate(row):
                if cell != 0:
                    top += 1
                    if cell > max_h[idx_r]:
                        max_h[idx_r] = cell
                        
                    if cell > max_c[idx_c]:
                        max_c[idx_c] = cell
                        
        return top + sum(max_h) + sum(max_c)
        