class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])
        x = [0] * m # num of server on a row
        y = [0] * n # num of server on a col
        for i in range(m):
            x[i] = sum(grid[i])
            
        tmp = zip(*grid)
        for i in range(n):
            y[i] = sum(tmp[i])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if x[i] + y[j] > 2: 
                        res += 1
                        
        return res
        
         