class Solution(object):
    def __init__(self):
        self.res = 0
        self.area = 0
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col:
                return
            if grid[r][c] != 1:
                return
            grid[r][c] = 0
            self.area += 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    self.area = 0
                    dfs(i, j)
                    
                    if self.area > self.res:
                        self.res = self.area
        return self.res