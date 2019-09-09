from math import sqrt
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def isPrime(num):
            if num >= 2:
                for i in range(2,int(sqrt(num))+1):
                    if not ( num % i ):
                        return False
            else:
                return False
            return True
        
        ans = 0
        
        for num in range(L, R+1):
            if isPrime(bin(num).count("1")):
                ans +=1
                
        return ans