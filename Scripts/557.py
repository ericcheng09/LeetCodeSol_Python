class Solution:
    def reverseWords(self, s):
        chars = s.split()
        out = []

        for i in range(len(chars)):
            out.append([])
            for char in chars[i]:    
                out[i].insert(0,char)
        words = []
        for w in out:
            words.append("".join(w))
        
        return " ".join(words)
            
        
      