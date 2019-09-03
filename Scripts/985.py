class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        s = sum([x for x in A if x%2 == 0])
        for offset, idx in queries:
            if A[idx]%2 == 0: s -= A[idx]
            A[idx] += offset
            if A[idx]%2 == 0: s += A[idx]
            
            ans.append(s)
        return ans