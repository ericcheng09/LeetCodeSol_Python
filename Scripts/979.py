# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.move = 0
        
        def calExcess(node):
            if not node: return 0
            left = calExcess(node.left) # coins are moved to or from left
            right = calExcess(node.right) # coins are moved to or from left right
            self.move += abs(left) + abs(right)
            return node.val - 1 + left + right # how many excess coins on this node 
            # negative: need coins from other nodes
            # positive: can push coin to other nodes
        calExcess(root)
        return self.move
        
        