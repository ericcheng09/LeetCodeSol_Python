class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in arr2:
            while True:
                try:
                    ans.append(arr1.pop(arr1.index(num)))
                except:
                    break
        ans += sorted(arr1)
        return ans