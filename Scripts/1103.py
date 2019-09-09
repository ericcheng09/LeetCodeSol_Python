from itertools import cycle
class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        ans = [0] * num_people
        n = 1
        idx = 0
        while candies>0:
            if candies > n:
                ans[idx%num_people] += n
            else:
                ans[idx%num_people] += candies
            candies -= n
            idx += 1
            n += 1
        return ans