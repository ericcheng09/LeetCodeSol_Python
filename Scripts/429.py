"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        levelDict = {}
        
        def travel(node, level):
            if node:
                if levelDict.get(level):
                    levelDict[level].append(node.val)
                else:
                    levelDict[level] = [node.val]
                
                if node.children:
                    for child in node.children:
                        travel(child, level + 1)
                        
            
        travel(root, 0)
        ans = []
        for i in range(len(levelDict)):
            ans.append(levelDict[i])
            
        return ans
            
            
        
        