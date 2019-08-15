class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # output = []
        # for num in A:
        #     if num % 2 == 0:
        #         output.insert(0, num)
        #     else:
        #         output.append(num)
        # return output
    
        return [num for num in A if not num % 2] + [num for num in A if num % 2]