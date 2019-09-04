class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        # distances = [(self.distance((0,0), point), point )for point in points]
        # distances.sort(key=lambda x: x[0])
        # ans = []
        # for i in range(K):
        #     ans.append(distances[i][1])
        # return ans
        
        return sorted(points, key= lambda x: x[0] ** 2 + x[1] ** 2)[:K]
         
    
    # def distance(self, p1, p2):
    #     return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2