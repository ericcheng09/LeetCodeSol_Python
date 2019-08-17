# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def removeTree(parentNode, child):
            if child == None: return
            removeTree(child, child.left)
            removeTree(child, child.right)

            if child.right or child.left:
                return
            elif child.val == 0:
                if parentNode.left == child:
                    parentNode.left = None
                else:
                    parentNode.right = None
            
        
        removeTree(root, root.left)
        removeTree(root, root.right)
        return root
        