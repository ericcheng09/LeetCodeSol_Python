# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # recursive
        self.maxDepth = 0
        def travel(node, level):
            if node:
                if level > self.maxDepth:
                    self.maxDepth = level
                travel(node.left, level + 1)
                travel(node.right, level + 1)
        travel(root, 1)    
        return self.maxDepth
    
        # using stack
        stack = [(root,1)]
        maxDepth = 0
        while stack:
            node, level = stack.pop()
            if node: 
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))
                if level > maxDepth:
                    maxDepth = level
        return maxDepth
        
        