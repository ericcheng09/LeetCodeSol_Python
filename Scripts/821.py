class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        ans = [0]*len(S)
        idxPre = S.index(C)
        for idx, s in enumerate(S):
            ans[idx] = abs(idx - idxPre)
            if idx == idxPre and idx+1 < len(S):
                try:
                    idxPre = S[idx+1:].index(C) + idx + 1
                except:
                    pass
        S = S[::-1]
        idxPre = S.index(C)
        ans_R = [0]*len(S)
        for idx, s in enumerate(S):
            ans_R[idx] = abs(idx - idxPre)
            if idx == idxPre and idx+1 < len(S):
                try:
                    idxPre = S[idx+1:].index(C) + idx + 1
                except:
                    pass
                
        ans_R.reverse()
        return [min(num) for num in zip(ans, ans_R)]
        
        