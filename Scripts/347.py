class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        # return heapq.nlargest(k, count.keys(), key=count.get) 
    
        countSorted = sorted(count.items(), key = (lambda x:x[1]), reverse=True)
        res = []
        for i in range(k):
            res.append(countSorted[i][0])
        return res