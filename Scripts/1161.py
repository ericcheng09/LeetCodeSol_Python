# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        levelSum = []
        def travelTree(node, level):
            if node == None:
                return
            if len(levelSum) < level:
                levelSum.append(node.val)
            else:
                levelSum[level - 1] += node.val
            travelTree(node.left, level + 1) 
            travelTree(node.right, level + 1) 
            
        travelTree(root, 1)
        
        return levelSum.index(max(levelSum)) + 1