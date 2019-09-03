class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
#         ans = ""
#         T = list(T)
#         for c in S:
            
#             while True:
#                 if c in T:
#                     ans += T.pop(T.index(c))
#                 else:
#                     break
#         while T:
#             ans += T.pop()
            
#         return ans
        ans = ""
        for c in S:
            ans += c*T.count(c)
            T = T.replace(c,"")
        ans += T
        return ans


       