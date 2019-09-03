class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        
        rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"];
        for word in words:
            uppers = list(word.upper())
            for idx, row in enumerate(rows):
                sameLineLen = 0
                for c in uppers:
                    if c not in row:
                        continue
                    sameLineLen += 1
                if sameLineLen == len(word):
                    ans.append(word)
                    
        return ans
                    
                            
                        