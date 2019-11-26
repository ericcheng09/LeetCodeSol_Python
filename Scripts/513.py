# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = None
        
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = (root.val, 0)
        self.travel(root, 0)
        return self.ans[0]
        
    def travel(self, node, level):
        if node == None:
            return 
        if not node.left and not node.right:
            # leaf node
            if self.ans[1] < level:
                self.ans = (node.val, level)
        
        self.travel(node.left, level + 1)
        self.travel(node.right, level + 1)
        