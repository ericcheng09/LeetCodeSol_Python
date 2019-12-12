# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        levelMax = [root.val]
        
        
        def travel(node, level):
            if node:
                if len(levelMax) < level + 1:
                    levelMax.append(node.val)
                elif levelMax[level] < node.val:
                    levelMax[level] = node.val
               
                
                travel(node.left, level + 1)
                travel(node.right, level + 1)
        
        
        travel(root, 0)
        
        return levelMax
            