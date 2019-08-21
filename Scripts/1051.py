class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        rightSeq = sorted(heights)
        ans = 0
        
        for idx, h in enumerate(heights):
            if h != rightSeq[idx]:
                ans += 1
                
        return ans