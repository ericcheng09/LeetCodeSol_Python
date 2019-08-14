# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        pre = root
        while(True):
            if pre.val > val:
                next_node = pre.left
            else:
                next_node = pre.right
            if next_node == None:
                if pre.val > val:
                    pre.left = TreeNode(val)
                else:
                    pre.right = TreeNode(val)
                break
            else:
                pre = next_node

        return root