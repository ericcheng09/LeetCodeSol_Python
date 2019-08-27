from collections import Counter
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        # intutive solution but slow
        # return [Counter(bin(number))["1"] for number in range(num + 1)]
        
        
        # follow the pattern
        # ex:
        # 0: 00
        # 1: 01
        
        # 2: 10 = 1 follow by 0's bits
        # 3: 11 = 1 follow by =1's bits
        
        # 4: 1_00 = 1 follow by 0's bits
        # 5: 1_01 = 1 follow by 1's bits
        # 6: 1_10 = 1 follow by 2's bits
        # 7: 1_11 = 1 follow by 3's bits
        
        bits = [0]
        power = 0
        idx = 0
        for i in range(1, num + 1):
            if i == 2 ** power:
                idx = 0
                power += 1
            bits.append(bits[idx] + 1)
            idx += 1
        return bits
        
        