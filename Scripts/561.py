class Solution:
    def arrayPairSum(self, nums):
        nums = sorted(nums)

        s = 0
        idx = len(nums)/2
        for i in range(int(idx)):
            s += nums[i * 2]
        return s
        """
        :type nums: List[int]
        :rtype: int
        """
        