class Solution:
    def fizzBuzz(self, n):
        out = list()
        for i in range(1,n+1):
            s = ''
            if i % 3 == 0:
                s += "Fizz"
                if i % 5 == 0:
                    s += "Buzz"
            elif i % 5 == 0:
                s += "Buzz"
            else: 
                s += str(i)
            out.append(s)
        return out
                
        """
        :type n: int
        :rtype: List[str]
        """
        