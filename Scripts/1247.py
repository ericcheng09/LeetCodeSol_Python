class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        xy, yx = 0, 0
        for idx in range(len(s1)):
            if s1[idx] != s2[idx]:
                if s1[idx] == "x":
                    xy += 1
                else:
                    yx += 1
        if (xy+yx) % 2:
            return -1
        
        return xy//2 + yx//2 + xy % 2 + yx%2
       
