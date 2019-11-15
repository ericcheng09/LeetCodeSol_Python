# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        nodes = []
        
        def travel(node, level):
            if node:
                if len(nodes) < level:
                    nodes.append([node.val])
                else:
                    nodes[level - 1].append(node.val)
                travel(node.left, level + 1)
                travel(node.right, level + 1)
        travel(root, 1)
        return [float(sum(x)) / len(x) for x in nodes]