"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
Idea:
    1. dfs and use stack to save the visited node sequence, 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from helper import *
from typing import List

class Solution:
    def pathSum(self, root:TreeNode, sum: int) -> List[List[int]]:
        def isLeaf(tree):
            return not (tree.left or tree.right)
        self.res = []
        def dfs(tree, sumi, stack):
            if tree:
                stack.append(tree.val)
                sumi += tree.val
                if sumi == sum and isLeaf(tree):
                    self.res.append(stack[:])  # stack[:] copys value instead of ref
                dfs(tree.left, sumi,stack)
                dfs(tree.right,sumi,stack)
                stack.pop()
            else:
                return None
        dfs(root,0,[])
        return self.res


if __name__ == '__main__':
    sl = Solution()
    tree = stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,5,1]")
    tmp = sl.pathSum(tree,22)
    print(tmp)

