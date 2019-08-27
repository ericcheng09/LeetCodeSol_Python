class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        textParts = text.split(" ")
        ans = []
        for idx in range(2, len(textParts)):
            if textParts[idx - 2] == first and textParts[idx - 1] == second:
                ans.append(textParts[idx])
        return ans