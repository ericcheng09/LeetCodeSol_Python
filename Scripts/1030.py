class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
#         distanceList = []
#         distanceDict = {}
#         for r in range(R):
#             for c in range(C):
#                 distance = abs(r - r0) + abs(c - c0)
#                 if distance not in distanceList:
#                     distanceList.append(distance)
#                     distanceDict[distance] = []
#                 distanceDict[distance].append([r, c])
#         distanceList.sort()
#         ans = []
#         for d in distanceList:
#             ans += distanceDict[d]
            
#         return ans

        distances = []
        for r in range(R):
            for c in range(C):
                distances.append((r,c, abs(r - r0) + abs(c - c0)))
                
        distances.sort(key=lambda d: d[2])
        
        return [d[0:2] for d in distances]
        