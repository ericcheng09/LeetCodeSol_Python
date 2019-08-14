class Solution:
    def selfDividingNumbers(self, left, right):
        out = list()
        for i in range(left,right+1):
            out.append(i)
            num = list()
            for char in str(i):
                num.append(int(char))
            for j in num:
                if j == 0 or i % int(j) != 0:
                    out.remove(i)
                    break
        return out