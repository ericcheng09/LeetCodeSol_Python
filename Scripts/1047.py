class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """   
        # 120 ms
#         strToRemove = []
#         while True:
#             pre = None
            
#             for idx, s in enumerate(S):
#                 if pre == s:
#                     strToRemove+=[s+s]
#                     pre = None
#                 pre = s

#             if strToRemove:
#                 for s in set(strToRemove):
#                     S = S.replace(s,"")
#                 strToRemove = []
#             else:
#                 break
#         return S   
    
    
        # refer to discussion:
        # 52 ms
        
        stack = []
        for c in S:
            if not stack or c != stack[-1]:
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)