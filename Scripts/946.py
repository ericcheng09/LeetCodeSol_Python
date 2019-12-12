class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # the nums in pushed need to be pushed into stack in order.
        # when the top of the stack is the number on top of popped, it needs to be pushed from stack immed, or the sequence will change
        stack = []
        for x in pushed:
            stack.append(x)
            
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        return len(stack) == 0 and len(popped) == 0