class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
     
        r, c = len(A), len(A[0])
        
        # invert
        for i in range(r):
            for j in range(c):
                A[i][j] = 1 if A[i][j] == 0 else 0
            A[i].reverse()
        return A