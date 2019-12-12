class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
#         sums = [0] * (len(nums) + 1)
#         sums[0] = 0
        
#         # sums[i] = the cummulative sum from first item to ith item
#         for idx, num in enumerate(nums):
#             sums[idx + 1] = sums[idx] + nums[idx] 
#         res = 0
#         # sums[j] - sums[i] = the sum of elements between jth to ith item ( j > i) (not include ith element)
#         for idx in range(len(nums)):
#             for idx_end in range(idx + 1, len(nums)+1):
#                 if sums[idx_end] - sums[idx] == k:
#                     res += 1
         
    
        # using dict
        res = 0
        s = 0 # the sum from start to current element
        d = {0:1} # used to record the occurance of sum that occur
        
        for num in nums:
            s += num # sum to current element
            
            # s - k: means upto current position, how many position that s - k occurs
            # if s - k exist, them from those positions sum to current element will be k
            #d[sum-k]：有多少位置（left），從開始加到目前，和為sum - k
            #res += d.get(s - k, 0)： 對所有left，從left一直加到目前，sum = k，’left->目前‘ 也就是subarray
            res += d.get(s - k, 0)
            
            d[s] = d.get(s, 0) + 1

            
        return res

    
    
    
        