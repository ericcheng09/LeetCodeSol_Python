# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.leaves = []
        self.nodeParent = {}
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
                
        def findlca(node): 
            # return: height of node & lca of node
            if node == None: 
                return 0, None
            
            # check the height of left and right subtree
            # (height of left/right, lca from left/right)
            # heigher subtree means deeper left
            # if same height, current node is lca
            leftheight, leftLca = findlca(node.left)
            rightheight, rightLca = findlca(node.right)
            # the height of this subtree = 1 + max(left, right)
            # lca = left/right or node if left and right are same heigh
            if rightheight > leftheight:
                return rightheight + 1, rightLca
            elif rightheight < leftheight:
                return leftheight + 1, leftLca
            else:
                # rightdepth == leftdepth
                # have same depth => this node must be the lca for its children
                return leftheight + 1, node        
        
        
        return findlca(root)[1]
        