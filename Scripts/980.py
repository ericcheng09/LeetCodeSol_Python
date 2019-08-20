class Solution(object):
    def __init__(self):
        self.counts_of_paths = 0
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        R, C = len(grid), len(grid[0])
        start_r, start_c = 0, 0
        end_r, end_c = 0, 0
        emptySpuares = 0

        
        
        # count num of spuares need to walk through, find the start and end square
        for idx_r, row in enumerate(grid):
            for idx_c, val in enumerate(row):
                if val != -1: emptySpuares += 1
                if val == 1:  start_r, start_c = idx_r, idx_c
                if val == 2:  end_r, end_c = idx_r, idx_c
                
        def findNeighbors(r, c):
            neighbors = []
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != -1:
                    neighbors.append((nr, nc))
            return neighbors
                
            
        def findPath(r, c, remainingSpuares):
            remainingSpuares -= 1
            if remainingSpuares < 0: return
            
            if remainingSpuares == 0 and r == end_r and c == end_c: 
                # reach the end and walk through every space exactly once
                self.counts_of_paths += 1
                return
        
            grid[r][c] = -1
            for nr, nc in findNeighbors(r,c):
                findPath(nr, nc, remainingSpuares)
            grid[r][c] = 0
        
        findPath(start_r, start_c, emptySpuares)
        
        return self.counts_of_paths