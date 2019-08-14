class Solution:
    def containsDuplicate(self, nums):
        num_dict = dict()
        out = False
        for num in nums:
            if num_dict.get(num) == None:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
        for k, v in num_dict.items():
            if v != 1:
                out = True
                break
        return out
            
        """
        :type nums: List[int]
        :rtype: bool
        """
        