class Solution(object):
    def __init__(self):
        self.res = []
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        self.permuString(S, 0, "")
        return self.res
    def permuString(self, S, idx,ans):
        if idx == len(S):
            self.res.append(ans)
        else:
            c = S[idx]
            if c.isalpha():
                self.permuString(S, idx + 1, ans + c.lower())
                self.permuString(S, idx + 1, ans + c.upper())
            else:
                self.permuString(S, idx + 1, ans + c)
        
            
            