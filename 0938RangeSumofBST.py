"""
Given the root node of a binary search tree,
return the sum of values of all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.

Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

Note:
    The number of nodes in the tree is at most 10000.
    The final answer is guaranteed to be less than 2^31.
Idea:
    1. inorder traversal method, add when meet the criteria, O(n)
    2. logn to find the first node, successor finding method takes O(1), O(logn +k)
    3. DFS, find the first node in range, then traversal subtrees. only visit node in criteria.
"""
from helper import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    cnt = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # inorder traversal
        def inorder(tree):
            if tree is None:
                return None
            inorder(tree.left)
            if L <= tree.val <= R:
                self.cnt += tree.val
            inorder(tree.right)
            return None

        inorder(root)
        return self.cnt

    def rangeSumBST2(self, root: TreeNode, L: int, R: int) -> int:
        # DFS
        def dfs(tree):
            if tree is not None:
                if L <= tree.val <= R:
                    self.cnt += tree.val
                if L < tree.val:
                    dfs(tree.left)
                if R > tree.val:
                    dfs(tree.right)

        dfs(root)
        return self.cnt


if __name__ == '__main__':
    sl = Solution()
    nums = "[10,5,15,3,7,13,18,1,null,6]"
    root = stringToTreeNode(nums)
    L = 6
    R = 10
    tmp = sl.rangeSumBST2(root, L, R)
    print(tmp)
