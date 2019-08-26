import math
class Solution(object):
    
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
    
        ans = []
        Level = int(math.log(label,2))
        currentLable = label
        while Level:
            parentMax = 2 ** (Level) - 1 # the max value of top level
            idx = math.ceil((currentLable - parentMax) / 2.0) # idx/offset of the current level
            ans.append(int(currentLable))
            currentLable = parentMax - idx + 1 
            Level -= 1
        
        ans.append(1)
        return ans[::-1]