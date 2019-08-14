# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.s = 0
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        
        self.bstToGst(root.right)
        self.s = self.s + root.val
        root.val = self.s
        self.bstToGst(root.left)
        
        return root