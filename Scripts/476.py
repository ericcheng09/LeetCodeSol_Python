class Solution:
    def findComplement(self, num):
        len_num = len(str(bin(num))[2:])
        return abs(2 ** len_num - num - 1)
        """
        :type num: int
        :rtype: int
        """
        