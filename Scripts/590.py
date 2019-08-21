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
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        def travel(node):
            if node: 
                for child in node.children:
                    self.postorder(child)
                self.ans.append(node.val)
        travel(root)
        return self.ans
            
            
            
            