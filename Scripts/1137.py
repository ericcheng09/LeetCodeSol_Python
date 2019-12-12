from functools import lru_cache
class Solution:
    @lru_cache(None)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        else:
            return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)


class Solution(object):
    def __init__(self):
        self.dp = {0:0, 1:1, 2:1}
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if self.dp.get(n):
            return self.dp.get(n)
        else:
            if n >= 3: self.dp[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            
        return self.dp[n]