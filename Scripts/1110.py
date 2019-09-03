# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        ans = []
        def travel(node, parent, LR):
            # LR: indicate this node is left or right child
            if node == None:
                return
            
            if node.val in to_delete:
                if LR == "L" and parent:    parent.left = None
                if LR == "R" and parent:    parent.right = None
                travel(node.left, None, "L")
                travel(node.right, None, "R")
            else:
                if parent == None:  ans.append(node)
                travel(node.left, node, "L")
                travel(node.right, node, "R")
                
        travel(root, None, None)

        return ans
                
