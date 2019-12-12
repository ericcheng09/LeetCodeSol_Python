class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        res = []
        tmp = []
        if len(nums) * len(nums[0]) != r*c:
            return nums
        
        for row in nums:
            for num in row:
                tmp.append(num)
                if len(tmp) == c:
                    res.append(tmp)
                    tmp = []
        return res
        