class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line = 1
        wordLength = 0
        for s in S:
            idx = ord(s) - ord("a")
            if wordLength + widths[idx] > 100:
                line += 1
                wordLength = widths[idx]
            else:
                wordLength += widths[idx]
        
        return [line, wordLength]