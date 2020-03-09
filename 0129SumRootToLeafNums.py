"""
Given a binary tree containing digits from 0-9 only, 
each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.

Example:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
Idea:
    1. dfs, start from root, recursively record the path, convert to int and return
"""
from helper import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def isLeaf(tree):
            return not(tree.left or tree.right)
        paths = []

        def dfs(tree, path):
            if tree is None:
                return None
            path += str(tree.val)
            if isLeaf(tree):
                paths.append(path[:])
            dfs(tree.left, path)
            dfs(tree.right, path)
            path = path[:-1]
        dfs(root, "")
        return sum(int(x) for x in paths)


if __name__ == '__main__':
    sl = Solution()
    tree = stringToTreeNode("[4,9,0,5,1]")
    tmp = sl.sumNumbers(tree)
    print(tmp)
