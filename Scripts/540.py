class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
#         c = collections.Counter(nums)
#         for key in c.keys():
#             if c[key] == 1:
#                 return key

#         return None

    
        def search(nums):
            mid = len(nums) // 2
            # length of nums will be 2k + 1
            # so if we spilt the list into 2 half
            # if the last 2 element on left halt are same,
            # then it meas that there are k pairs on the left,
            # so we need to search right haft
            if len(nums) == 1:
                return nums[0]
            
            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    return search(nums[:mid-1 ])
                else:
                    return search(nums[mid:])
            else:
                if nums[mid] == nums[mid - 1]:
                    return search(nums[mid+1:])
                else:
                    return search(nums[:mid])


        return search(nums)