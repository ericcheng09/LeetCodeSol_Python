# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0: return None
        root = TreeNode(preorder[0])    
        root.left = self.bstFromPreorder([A for A in preorder if A < root.val])
        root.right =  self.bstFromPreorder([A for A in preorder if A > root.val])
        return root