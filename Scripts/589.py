"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def __init__(self):
        self.ans = []
        
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # recursive 
        def travel(node):
            if node: 
                self.ans.append(node.val)
                for child in node.children:
                    self.preorder(child)
                
        travel(root)
        return self.ans