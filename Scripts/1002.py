from collections import Counter
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """

        wordCounters = list(map(Counter, A))
        ans = []
        tmp = wordCounters.pop(0)
        for counter in wordCounters:
            tmp = tmp & counter 
        
        for k, v in tmp.items():
            for i in range(v):
                ans.append(k)
        return ans
            
