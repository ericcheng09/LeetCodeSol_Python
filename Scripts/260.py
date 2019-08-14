class Solution:
    def singleNumber(self, nums):
        out = list()
        num_dic = dict()
        for num in nums:
            if num_dic.get(num) == None:
                num_dic[num] = 1
            else:
                num_dic[num] += 1
        
        for k, v in num_dic.items():
            if v == 1:
                out.append(k)
        return out
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        