class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = [a for a in A if a % 2 != 0]
        even = [a for a in A if a % 2 == 0]
        
        return [num for sublist in zip(even, odd) for num in sublist]