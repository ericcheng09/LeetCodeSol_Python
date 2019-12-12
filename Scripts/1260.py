class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        
        nums = [num for row in grid for num in row]
        start_idx = (m*n) - k % (m*n)
        nums =  nums[start_idx:] + nums[:start_idx]
        res = []
        a = iter(nums)

        for _ in range(m):
            tmp = []
            for _ in range(n):
                tmp.append(next(a))
            res.append(tmp)
            
        return res