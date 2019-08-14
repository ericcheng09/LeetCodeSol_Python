class Solution:
    def islandPerimeter(self, grid):
        peri = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    peri += 4
                    for h in range(-1,2,2):
                        if j + h >= 0 and j + h <= len(grid[i]) - 1:
                            if grid[i][j + h] == 1:
                                peri -= 1
                    for v in range(-1,2,2):
                        if i + v >= 0 and i + v <= len(grid) - 1:
                            if grid[i + v][j] == 1:
                                peri -= 1
        return peri
        """
        :type grid: List[List[int]]
        :rtype: int
        """
    