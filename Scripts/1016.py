class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        for i in xrange(1, N + 1):
            if bin(i)[2:] not in S:
                return False
        return True