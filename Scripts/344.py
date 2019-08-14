class Solution:
    def reverseString(self, s):
        l = len(s) - 1
        out = ""
        for i in range(len(s)):
            out += s[l - i]
        return out
            
        """
        :type s: str
        :rtype: str
        """
        