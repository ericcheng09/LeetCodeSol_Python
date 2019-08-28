class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        minusN = nums[0] * nums[1]
        secondXthird = nums[-2] * nums[-3]
        bigger = secondXthird if secondXthird > minusN else minusN
        return nums[-1]*bigger