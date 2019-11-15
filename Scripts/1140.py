class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        self.memo = {} 
        weight = [0]
        for i in range(len(piles)):
            weight += [weight[-1] + piles[-1-i]]
        weight.reverse()
        weight.pop() 
        # weight = remain stone can get from ith pile
        def dp(i,M):
            if (i,M) not in self.memo:
                if len(piles) - i <= 2*M: 
                    # take all remaining
                    self.memo[(i,M)]= weight[i]
                else:
                    tmp = 0
                    for k in range(1,2*M+1): # 1<=x<=2M
                        new_M = max(M,k)
                        tmp = max(tmp,weight[i]-dp(i+k,new_M)) # dp(i+k,new_M) is the max stone the other player can get
                    self.memo[(i,M)] = tmp
            return self.memo[(i,M)] # maximum stone can get from ith pile with M
        return dp(0,1)