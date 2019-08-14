class Solution:
    def checkPerfectNumber(self, num):
        if num == 1:
            return False
        s = 1
        for i in range(2,num):
            if i * i > num:
                break
            if num % i == 0:
                s += i
                if i * i != num:
                    s += num / i
        return s == num
        
            
                
        """
        :type num: int
        :rtype: bool
        """
        