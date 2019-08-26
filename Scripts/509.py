class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
#         # recursively
#         if N == 0:
#             return 0
#         if N == 1:
#             return 1
        
#         return self.fib(N-1) + self.fib(N-2)
        
        # iterativly
        fiblist = [0, 1]
        for idx in range(2, N + 1):
            fiblist.append(fiblist[idx - 1] + fiblist[idx - 2])
        
        return fiblist[N]