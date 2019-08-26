class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        row, col = len(A), len(A[0])
        score = 0
        
        # the left-most column could contribute the highest score
        for y in range(row):
            if A[y][0] == 0:
                # filp row
                for x in range(col):
                    A[y][x] = A[y][x] ^ 1 # xor
        score += row * (2 ** (col - 1))
        for x in range(1, col):
            numOfones = 0
            for y in range(row):
                if A[y][x] == 1:
                    numOfones += 1
            numOfzeros = row - numOfones
            if numOfones < numOfzeros:
                # should flip column
                # calculate the max score here instead
                score += numOfzeros * (2 ** (col - x - 1))
            else:
                score += numOfones * (2 ** (col - x - 1))
                
        return score
                
                
                