class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        maxN = A[0]
        minN = A[0]
        
        for num in A:
            if num > maxN:
                maxN = num
            if num < minN:
                minN = num
        tmp = maxN - minN
    
        if (tmp / 2) < K:
            return 0
        else:
            return maxN - minN - 2*K 
