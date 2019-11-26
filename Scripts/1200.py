class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        if len(arr) <= 1 or arr == None:
            return []
        arr.sort()
        res = []
        pre = arr[0]
        minimum = arr[-1] - arr[0]
        for num in arr[1:]:
            tmp = num - pre
            if tmp < minimum:
                minimum = tmp
                res = []
            if tmp == minimum:
                res.append([pre, num])
            pre = num
        return res