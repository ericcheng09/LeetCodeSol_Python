class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = [0]
         
        for s in S:
            if s == "(":
                stack.append(0)
            else:   
                # a closed Parentheses
                v = stack.pop() 
                stack[-1] += max(2 * v, 1)
                # only it is (A), the "v" will not equal to 0.
                # if v = 0, means that current closed parentheses is singal one ()
        return stack.pop()