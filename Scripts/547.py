class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.visted = []
        ans = 0
        for i in range(len(M)):
            if i not in self.visted:
                ans += 1
                self.visted.append(i)
                self.dfs(i, M)
        return ans
    
    def dfs(self, i, M):
        for j in range(len(M)):
            if j not in self.visted and M[i][j] == 1:
                self.visted.append(j)
                self.dfs(j, M)