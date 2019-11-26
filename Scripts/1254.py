class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x_len, y_len = len(grid), len(grid[0])
        def dfs(x, y):
            if x < 0 or x >= x_len or y < 0 or y >= y_len:
                return
            if grid[x][y] != 0:
                return
            
            
            grid[x][y] = 1
            dfs(x, y - 1)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x + 1, y)
        
        for x in range(x_len):
            dfs(x, y_len - 1)
            dfs(x, 0)
        for y in range(y_len):
            dfs(x_len - 1, y)
            dfs(0, y)
        res = 0
        for x in range(x_len):
            for y in range(y_len):
                if grid[x][y] == 0:
                    res += 1
                    dfs(x, y)
        return res