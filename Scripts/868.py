class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N)[2:]
        longestD = 0
        stack = []
        for b in s:
            if not stack and b == "1":
                stack.append(b)
            elif stack:
                stack.append(b)
                if b == "1":
                    stack.pop()
                    tmp = 1
                    while stack[-1] != "1":
                        stack.pop()
                        tmp += 1
                    if tmp > longestD:
                        longestD = tmp
        return longestD
                
        