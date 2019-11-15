class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        d = {}

        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1

        return [num for num, count in d.items() if cnt > 1]