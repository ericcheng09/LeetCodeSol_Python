from functools import lru_cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        # dynamic programming
        N = len(days)
        durations = [1, 7, 30]
        
        @lru_cache(None) # this decorator can cache the result of function call
        def dp(i): # how much (minimum) money to spend from day[i] to end of the plan (days[-1])
            if i >= N:
                return 0
            
            ans = float('inf')
            # dp(i)=min(dp(j1)+costs[0],dp(j7)+costs[1],dp(j30)+costs[2])
            j = i
            for cost, duration in zip(costs, durations):
                while j < N and days[j] < days[i] + duration:
                    j += 1
                ans = min(ans, dp(j) + cost)
            return ans
        
        
        return dp(0)
                
                