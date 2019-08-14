class Solution:
    def hammingDistance(self, x, y):
        count = 0
        a = list()
        b = list()
        
        for char in str(bin(x))[2:]:
            a.append(char)
        for char in str(bin(y))[2:]:
            b.append(char)
       
        if len(a) > len(b):
            for i in range(abs(len(a)-len(b))):
                b.insert(0,'0')
        else:
            for i in range(abs(len(a)-len(b))):
                a.insert(0,'0')
        
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count