class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        output = [a**2 for a in A]
        output.sort()
        return output