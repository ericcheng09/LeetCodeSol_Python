class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = [0] * len(S)
        high = len(S)
        low = 0
        
        for idx, s in enumerate(S):
            if s == "I":
                ans[idx] = low
                low += 1
            else:
                ans[idx] = high
                high -= 1
                
        return ans + [high]
        