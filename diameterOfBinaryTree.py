# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Given a binary tree, compute length of diameter, longest way between any two nodes.
input: root of a binary tree
output: diameter int
extreme case:
    1. empty tree, return 0, init diameter as 1, when 1/0 node, max(1+0+0,1)=1  
idea: use Depth First Search method, 
    1. find the longest in the left L, and longest in the right R, 
    2. check the length if it's larger than L+R+1, update diameter
    3. return max(L,R)+1, 1 for the root
    4. recursively
    5. because L and R will count the node, edge is 1 less
"""


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 1  # initialize as 1 to solve []

        def dfs(tree: TreeNode) -> int:
            if tree is None:
                return 0
            L = dfs(tree.left)
            R = dfs(tree.right)
            self.diameter = max(L + R + 1, self.diameter)
            return max(L, R) + 1

        dfs(root)
        return self.diameter - 1

#
