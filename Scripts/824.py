class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split(" ")
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        for idx, word in enumerate(words):
            if word[0] in vowels:
                words[idx] += "ma" + "a" * (idx + 1)
            else:
                words[idx] = word[1:] + word[0] + "ma" + "a" * (idx + 1)
                
        return " ".join(words)
        
            