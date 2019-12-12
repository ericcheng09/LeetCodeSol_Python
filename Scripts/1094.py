class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        points = [0] # changes of num of passengers at locations that pick or drop off them
        
        for num, start, end in trips:
            while len(points) <= end:
                points.append(0)
            points[start] += num
            points[end] -= num
            
            
        for i in range(1, len(points)):
            points[i] += points[i - 1]
            
            if points[i] > capacity:
                return False
            
            
        return True
        