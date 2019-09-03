# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.leavesOne = self.travel(root1)
        self.leavesTwo = self.travel(root2)
        return self.leavesOne == self.leavesTwo
        
    def travel(self, root):
        tmp = []
        def getleaves(node):
            if node == None:
                return 
            getleaves(node.left)
            if not node.left and not node.right:
                # is a leave
                tmp.append(node.val)
            getleaves(node.right)
            
        getleaves(root)
        return tmp