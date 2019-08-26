"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # recursively
        if root == None:
            return 0
        
        if root.children: 
            return 1 + max([self.maxDepth(child) for child in root.children])
        else:
            return 1
       
            
        # iterative solution: refer to discussion   
#         if root == None:
#             return 0

#         stack = [[root, 1]]
#         res = 0
#         while stack != []:
#             node, depth = stack.pop(0)
#             res = max(depth, res)
#             if node.children:
#                 for child in node.children:
#                     stack.append([child, depth + 1])
#         return res