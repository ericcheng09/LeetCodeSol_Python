class Solution:
    def findMaxLength(self, nums):
        w = dict()
        w[0] = 1
        w[1] = -1
        max_l = 0
        s = 0
        t = dict(list())
        t[0] = [-1]
        for idx in range(len(nums)):
            s += w[nums[idx]]
            if t.get(s) == None:
                t[s] = [idx]
            else:
                t[s].append(idx)
            
        length = list()
        for k, v in t.items():
            length.append(v[-1] - v[0])
        if len(length) > 0:
            return max(length)
        else:
            return 0
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        