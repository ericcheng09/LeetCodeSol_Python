import collections
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        words = collections.Counter(A.split(" ") + B.split(" "))

        return [word for word in words if words[word] == 1]
            