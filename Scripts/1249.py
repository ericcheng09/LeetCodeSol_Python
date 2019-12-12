class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        idx_l_stack = []
        idx_r_stack = []
        res = ""
        for idx, char in enumerate(s):
            if char == "(":
                idx_l_stack.append(idx)
            elif char == ")":
                if idx_l_stack:
                    idx_l_stack.pop()
                else:
                    idx_r_stack.append(idx)
        return "".join([s[i] for i in range(len(s)) if i not in idx_l_stack and i not in idx_r_stack ])