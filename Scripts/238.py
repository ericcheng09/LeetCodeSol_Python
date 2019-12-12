class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        l = len(nums)
        left, right, res = [0] * l, [0] * l, [0] * l
        # left: store the product of all elemnet to the left (not include nums[i])
        # right: store the product of all elemnet to the right (not include nums[i])
        left[0] = 1
        right[l - 1] = 1
        for i in range(1, l):
            left[i] = left[i - 1] * nums[i - 1]
            
        for i in reversed(range(l - 1)):
            right[i] = right[i + 1] * nums[i + 1]
        for i in range(l):
            res[i] = left[i] * right[i]    
        
        return res