import collections
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        cout = collections.Counter(arr)
        
        return cout.most_common(1)[0][0]