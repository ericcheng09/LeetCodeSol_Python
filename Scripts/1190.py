class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        tmp = [""]
        i = 0
        for c in s:
            if c == "(":
                tmp.append("") 
            elif c == ")":
                text = tmp.pop()[::-1]
                tmp[-1] += text
            else:
                tmp[-1] += c
        return tmp[-1]