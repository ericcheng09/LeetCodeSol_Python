# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import re
class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        nodes = [(len(s[1]), int(s[2])) for s in re.findall("((-*)(\d+))", S)]
        # refer to https://docs.python.org/3/library/re.html
        # example output: [(0, 1), (1, 2), (2, 3), (2, 4), (1, 5), (2, 6), (2, 7)] 
        
        # Refer to Solution
        # def recusrive(level):
        #     if len(nodes) == 0 or level != nodes[0][0]:
        #         return None
        #     node = TreeNode(nodes[0][1])
        #     nodes.remove(nodes[0])
        #     node.left = recusrive(level + 1)
        #     node.right = recusrive(level + 1)
        #     return node
        # return recusrive(0)
        
        # Iterative version by myself
        def iterative():
            parentMap = dict() # record the parent of each level 
            parentMap[1] = TreeNode(nodes[0][1]) 
            level = 1 
            for node in nodes[1:]:
                if node[0] == level and parentMap[level].left == None:
                    parent = parentMap.get(level)
                    parent.left = TreeNode(node[1])
                    level += 1 # next level to construct
                    parentMap[level] = parent.left
                elif node[0] == level and parentMap[level].left != None:
                    parent.right = TreeNode(node[1])
                    level += 1 # next level to construct
                    parentMap[level] = parent.right
                elif node[0] < level: 
                    # if the level of node is smaller than level expect to construct -> no deeper node in the left of this subtree
                    for k, v in parentMap.items():
                        if k > node[0]:
                            parentMap[k] == None
                    parent = parentMap.get(node[0])
                    parent.right = TreeNode(node[1])
                    level = node[0] + 1
                    parentMap[level] = parent.right
            return parentMap[1]
        
        return iterative()
