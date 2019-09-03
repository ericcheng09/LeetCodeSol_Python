class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            y = stones.pop(stones.index(max(stones)))
            x = stones.pop(stones.index(max(stones)))
            
            if y != x:
                stones.append(y-x)
                
        if stones:
            return stones[-1]
        else:
            return 0
                