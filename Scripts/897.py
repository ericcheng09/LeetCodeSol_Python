# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        values = []
        
        def search(node):
            if node == None: return
            search(node.left)
            values.append(node.val)
            search(node.right)
            
        search(root)
        
        root = TreeNode(values.pop(0))
        tmp = root
        while values:
            tmp.right = TreeNode(values.pop(0))
            tmp = tmp.right
        
        return root
            
        
            