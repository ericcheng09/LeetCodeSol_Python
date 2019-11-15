# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def travel(node, pre):
            if node:
                if not node.left and not node.right:
                    # reach leaf
                    self.ans += pre * 2 + node.val
                # print pre
                travel(node.left, pre * 2 + node.val)
                travel(node.right, pre * 2 + node.val)
                    
        travel(root, 0)
        return self.ans