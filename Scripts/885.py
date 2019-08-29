from itertools import cycle
class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
#         # 112 ms
#         ans = []
#         direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         dirIdx = 0
#         length = 1
#         currentVisitedLength = 0
#         move = 0
#         while len(ans) < R * C:
#             if 0 <= r0 < R and 0 <= c0 < C:
#                 ans.append([r0, c0])
#             if currentVisitedLength == length:
#                 currentVisitedLength = 0
#                 move += 1
#                 dirIdx += 1
#                 dirIdx = dirIdx%4
#                 if move % 2 == 0:
#                     length += 1
#             if currentVisitedLength < length:
#                 offsetR, offsetC = direction[dirIdx]
#                 r0 += offsetR
#                 c0 += offsetC
#                 currentVisitedLength += 1
#         return ans
    
        # 92 ms
        ans = []
        direction = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
        lengthOffset = cycle([0 , 1])
        length = 1
        currentVisitedLength = 0
        while len(ans) < R * C:
            offsetR, offsetC = next(direction)
            while currentVisitedLength < length:
                if 0 <= r0 < R and 0 <= c0 < C:
                    ans.append([r0, c0])
                r0 += offsetR
                c0 += offsetC
                currentVisitedLength += 1
            currentVisitedLength = 0
            length += next(lengthOffset)
           
        return ans