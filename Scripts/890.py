class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        seenInPattern = []
        patternInNumber = []
        # convert patter into a number list
        for s in pattern:
            if s not in seenInPattern:
                seenInPattern.append(s)
                patternInNumber.append(seenInPattern.index(s))
            else:
                patternInNumber.append(seenInPattern.index(s))
       
        for w in words:
            seenInWord = []
            wordInNumber = []    
            for s in w:
                if s not in seenInWord:
                    seenInWord.append(s)
                    wordInNumber.append(seenInWord.index(s))
                else:
                    wordInNumber.append(seenInWord.index(s))
            if wordInNumber == patternInNumber:
                ans.append(w)
                
            
        return ans
            
        # refer to solution
        
        # def match(word):
        #     m1 = {}
        #     m2 = {}
        #     for w, p in zip(word, pattern):
        #         if w not in m1: m1[w] = p
        #         if p not in m2: m2[p] = w
        #         if (m1[w], m2[p]) != (p, w):
        #             return False
        #     return True
        # return filter(match, words)