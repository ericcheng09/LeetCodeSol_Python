class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        operationDict = {"&":all, "|": any, "!": lambda x: not x[0] }
        stack = []
        operator = []
        conunt_stack = []

        for e in expression:
            if e == ",":
                conunt_stack[-1] += 1
            elif e == "t":
                stack.append(True)
            elif e == "f":
                stack.append(False)
            elif e == "&" or e == "!" or e == "|":
                operator.append(operationDict.get(e))
            elif e == "(": # new expression
                conunt_stack.append(1)
            elif e == ")": # closed
                numPop = conunt_stack.pop()
                tmp = []
                for _ in range(numPop):
                    tmp.append(stack.pop())
               
                operation = operator.pop()
                res = operation(tmp)
                stack.append(res)
            
        return stack.pop()