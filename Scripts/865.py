# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        depth = {None: -1}
        def dfs(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        
        max_depth = max(depth.values())

        
        def answer(node):   
            #  find the deepest node that can be find at the subtree of this node
            if not node or depth.get(node, None) == max_depth:
                return node
            L, R = answer(node.left), answer(node.right)
            
            
            # if we can find deepest node from both left and right means this subtree is the subtree we want
            # otherwise, if either left or right side have deepest node then it means this node is not the root of the subtree we want, we need to go up one level to find root of the subtree.
            # if both left and right have not deepest node, and this subtree is not the tree we want
            return node if L and R else L or R
        return answer(root)
            