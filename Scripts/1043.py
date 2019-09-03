class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        # refer to discussion
        # dynamic programming
        dp = [0]*(len(A) + 1) # the maximum sum can get from A[0] ~ A[i]
        for i in range(len(A)):
            cur_max = 0
            for k in range(K):
                if i - k >= 0: # check the last 1 ~ 3 numbers
                    cur_max = max(cur_max, A[i - k])
                    # check if the partition can give larger sum value
                    dp[i + 1] = max(dp[i + 1], dp[i - k] + cur_max*(k + 1))
        return dp[-1]      