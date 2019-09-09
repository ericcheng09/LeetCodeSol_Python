class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # These answers refer to the solution and discussions
        
        # Alex always wins
        # return True
    
        # recursive (Time limit exceed)
#         N = len(piles)
#         # alex get stones: score increase
#         # lee get stones: score decrease
#         # score > 0 alex wins
#         def dp(i, j): # the stones can get when piles[i] ~ piles[j] remains
#             # The value of the game [piles[i], piles[i+1], ..., piles[j]].
#             if i > j: return 0
#             parity = (j - i - N) % 2
#             if parity == 1:  # first player
#                 return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
#             else:
#                 return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

#         return dp(0, N - 1) > 0
    
        # DP
        l = len(piles)
        dp = [[None for i in range(l)] for j in range(l)]
        parity =0

        
        dp[i][j] # the score can get if remaining stones[i:j]
        def ans(i,j):

            if dp[i][j] is not None :
                return dp[i][j]
            if i==j or i > j:
                return 0
           

            parity = ( j - i + 1)  % 2  
            if parity ==0 : # alex's turn
                dp[i][j] = max( piles[i] + ans(i+1,j) , piles[j] + ans(i,j-1) ) 
            else :
                dp[i][j] = max( -piles[i] + ans(i+1,j), -piles[j] + ans(i,j-1) )    
            return dp[i][j]


        return ans(0, l-1 ) > 0\