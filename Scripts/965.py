# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        treeValue = 0
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        treeValue = root.val
        
        def checkUnivalue(node):
            if not node: return True
            if node.val != treeValue:
                nodeEql = False
            else:
                nodeEql = True
            left = checkUnivalue(node.left)
            right = checkUnivalue(node.right)
            if left and right and nodeEql:
                return True
            else:
                return False
        
        return checkUnivalue(root)