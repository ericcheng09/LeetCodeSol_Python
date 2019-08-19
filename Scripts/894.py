# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    record = {0: [], 1:[TreeNode(0)]} # cache the ans of different N
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        # full binary tree with N nodes= root + left full binary tree with x nodes + right full binary tree with N - x - 1 nodes
        if N not in Solution.record:
            ans = []
            for x in range(N): # recursive find the answers (full binary trees) from 0 nodes to N nodes
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        tree = TreeNode(0)
                        tree.left = left
                        tree.right = right
                        ans.append(tree)
            Solution.record[N] = ans

        return Solution.record[N]
    