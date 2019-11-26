class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        square_L = len(A)
        dp = []
        for _ in range(square_L):
            dp.append([0] * square_L)
        
        # let dp[r][c] be the minimum weight can get start from row r anc column c
        dp[-1] = list(A[-1])


        for r in range(square_L - 2,-1,-1): # from 2nd last row to first row 
            for c in range(square_L):
                dp[r][c] = A[r][c] + min(dp[r+1][max(0, c-1): min(c+2, square_L)])
                
                # need to deal with boundary
        return min(dp[0])