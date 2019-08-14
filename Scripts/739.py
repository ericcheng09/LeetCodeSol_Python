class Solution:
    def dailyTemperatures(self, temperatures):
        out = list()
        temperatures.reverse()
        pos = dict()
        
        for i in range(len(temperatures)):
            pos[temperatures[i]] = i
            out.append(0)
            temp = list()
            for j in range(temperatures[i] + 1 , 101):
                if pos.get(j) == None:
                    continue
                else:
                    temp.append(i - pos[j])
            if len(temp) > 0:
                out[i] = min(temp)
        out.reverse()
        return out
                    
                
                    
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """