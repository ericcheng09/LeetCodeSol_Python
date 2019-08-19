class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        ans = 0
        charCount = {}
        for c in chars:
            if c not in charCount:
                charCount[c] = 1
            else:
                charCount[c] += 1
        for word in words:
            temp = {}
            good = True
            for c in word:
                if c not in temp:
                    temp[c] = 1
                else:
                    temp[c] += 1
            for k, v in temp.items():
                if charCount.get(k):
                    if not v <= charCount.get(k):
                        good = False
                        break
                else:
                    good = False
                    break
            if good:
                ans += len(word)
        return ans