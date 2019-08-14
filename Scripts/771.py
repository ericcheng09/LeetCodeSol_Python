class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for c in J:
            count = count + S.count(c)
            # str.count(substring): count the occurance of substring in str
        return count
