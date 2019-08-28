class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        
        # we need to focus on nested parentheses which may contribute deeper VPS depth
        # the best way to do is to separate nested VPS(Q) into 2 VPS(C,D) which maxdepth(C,D)
        # is ceil(Q.depth / 2)
        ans = [0]
        pre = seq[0]
        mark = 0
        for c in seq[1:]:
            if c == pre:
                mark = 0 if ans[-1]  else 1
            ans.append(mark)
            pre = c
        return ans
        