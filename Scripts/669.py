# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        
        
        def travelNtrim(node):
            if node == None:
                return
            elif node.val > R: # node in right subtree are all larger than R
                return travelNtrim(node.left)
            elif node.val < L: # node in left subtree are all larger than R
                return travelNtrim(node.right)
            else:
                # between L and R
                # trim left and R
                node.left = travelNtrim(node.left) 
                node.right = travelNtrim(node.right)
                return node
        return travelNtrim(root)