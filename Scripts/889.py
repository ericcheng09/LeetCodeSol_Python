# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        # https://www.techiedelight.com/construct-full-binary-tree-from-preorder-postorder-sequence/
        # a unique binary tree can't be constructed with pre- and post-order traversal
        # but a unique full binary tree can
        
        # pre: root + preorder of left subtree + preorder of right subtree
        # post: postorder of left subtree + postorder of right subtree + root
        # we could recursively solve this by split the pre traversal into left and right subtree and connect the root to them
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root
        
        length_leftNodes = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:length_leftNodes+1], post[:length_leftNodes])
        root.right = self.constructFromPrePost(pre[length_leftNodes+1:], post[length_leftNodes:-1])
        return root