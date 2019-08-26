class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        boundaryIdx = len(board) - 1
       
        ans = 0
        for idx_row, rows in enumerate(board):
            for idx_col, cell in enumerate(rows):
                # if space == ".":
                if cell == "R":
                    R = (idx_row, idx_col)
                    break
        
        for v, h in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            idx_row, idx_col = R
            while True:
                idx_row += v
                idx_col += h
                if idx_row < 0 or idx_row > boundaryIdx or idx_col < 0 or idx_col > boundaryIdx:
                    break
                    
                cell = board[idx_row][idx_col]
                if cell == ".":
                    continue
                if cell == "B":
                    break
                if cell == "p":
                    ans += 1
                    break
        
        return ans
      