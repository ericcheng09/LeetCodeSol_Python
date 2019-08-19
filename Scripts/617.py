# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # Sol#1 : 88ms and 13.2 MB
#         if t1 == None and t2 == None:
#             return None
#         elif t1 == None and t2: 
#             root = TreeNode(t2.val)
#         elif t1 and t2 == None: 
#             root = TreeNode(t1.val)
#         else:
#             root = TreeNode(t1.val + t2.val)
            
#         root.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
#         root.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        # Sol#2: 80ms 12.8Mb
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)   
        
        return t1