class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = sum(A)
        sumB = sum(B)
        A = set(A)
        B = set(B)
        for x in A:
            if x + (sumB - sumA) / 2 in B:
                return [x, x + (sumB - sumA) / 2]