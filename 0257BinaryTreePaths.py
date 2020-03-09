"""
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Example:
Input:
   1
 /   \
2     3
 \
  5
Output: ["1->2->5", "1->3"]
Explanation: All root-to-leaf paths are: 1->2->5, 1->3
Idea:
    1. dfs to get all path
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from helper import *


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def isLeaf(tree):
            return not(tree.left or tree.right)
        paths = []

        def dfs(tree: TreeNode, path):
            if tree is None:
                return None
            else:
                if path:
                    path += "->"+str(tree.val)
                else:
                    path = str(tree.val)
                if isLeaf(tree):
                    paths.append(path[:])
                    return None
                else:
                    dfs(tree.left, path)
                    dfs(tree.right, path)
                    path = path[:-3]
            return None

        dfs(root, "")
        return paths


if __name__ == '__main__':
    sl = Solution()
    tree = stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,5,1]")
    tmp = sl.binaryTreePaths(tree)
    print(tmp)
