class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        
        answer = []
        def findpath(node, path):
            pathToHere = path + [node]
            for next_node in graph[node]:
                findpath(next_node, pathToHere)
            if node == len(graph) - 1: answer.append(pathToHere)
        findpath(0, [])
        return answer