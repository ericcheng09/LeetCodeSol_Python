class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        idxA = 0
        idxB = 0
        while idxA < len(A) and idxB < len(B):
            startA, endA = A[idxA]
            startB, endB = B[idxB]
            tmp = [max(startA, startB), min(endA, endB)]
            if tmp[0] <= tmp[1]:
                # overlap
                ans.append(tmp)
            
            if A[idxA][1] < B[idxB][1]:
                idxA += 1
            else:
                idxB += 1
            
        return ans