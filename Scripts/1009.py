class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary_str = bin(N)[2:]
        tmp = 2 ** len(binary_str) - 1
        return tmp - N

        