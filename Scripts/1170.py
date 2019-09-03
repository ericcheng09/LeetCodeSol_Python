class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        ans = []
        wordF = []
        
        def f(word):
            word = sorted(list(word))
            return word.count(word[0])
            
        for word in words:
            wordF.append(f(word))
        wordF.sort()
        
        for query in queries:
            F = f(query)
            count = 0
            for n in wordF:
                if n > F:
                    count += 1
            ans.append(count)
        return ans
