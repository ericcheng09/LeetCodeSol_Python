class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        left = 0
        right = 0
        ans = 0
        for s in S:
            if s == "(": 
                left += 1
            if s == ")": 
                if left == 0:
                    right += 1
                else:
                    left -= 1
            
        return left + right
    
    
        # remove all vaild parenthese pairs, remaining will the number needs to add
        # while True:
        #     S = S.replace("()","")
        #     try:
        #         S.index("()")
        #     except:
        #         break
        # return len(S)