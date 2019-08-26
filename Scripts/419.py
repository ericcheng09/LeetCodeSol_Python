class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        
        # check the left and up of the "X"
        for idx_row, rows in enumerate(board):
            for idx_col, space in enumerate(rows):
                if space == "X":
                    if (idx_col == 0 or board[idx_row][idx_col - 1] == ".") and (idx_row == 0 or board[idx_row - 1][idx_col] == "."):
                        count += 1
        return count