class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        prims = []
        tmp = ""
        count, prim_idx = 0, 0
        output = ""
        for s in S:
            if s == "(":
                count += 1
            if s == ")":
                count -= 1
            tmp = tmp + s
            if count == 0:
                prims.append(tmp)
                print tmp
                tmp = ""
                prim_idx += 1
        output = ""  
        for prim in prims:
            output += prim[1:-1]
            
        return output