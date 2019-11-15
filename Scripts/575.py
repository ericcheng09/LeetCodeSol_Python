class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # the mamimum kinds sister can get is n/2
        # we could count the number of unique kinds in candies
        return min(len(candies)/2, len(set(candies)))