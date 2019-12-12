class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if sum(A) % 3 != 0:
            return False
        target = sum(A) / 3
        tmp = 0
        partition = 0
        for num in A:
            tmp += num
            if tmp == target:
                partition += 1
                tmp = 0
                
        if partition == 3:
            return True
        else:
            return False