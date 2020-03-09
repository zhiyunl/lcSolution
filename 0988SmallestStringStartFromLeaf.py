"""
Given the root of a binary tree, each node has a value from 0 to 25 representing 
the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b',
 and so on.
Find the lexicographically smallest string that starts at a leaf of this tree 
and ends at the root. (As a reminder, any shorter prefix of a string is 
lexicographically smaller: for example, "ab" is lexicographically smaller 
than "aba".  A leaf of a node is a node that has no children.)

Example 1:
Input: [0,1,2,3,4,3,4]
Output: "dba"

Example 2:
Input: [25,1,3,1,3,0,2]
Output: "adz"

Example 3:
Input: [2,2,1,null,1,0,null,0]
Output: "abc"

Note:

    The number of nodes in the given tree will be between 1 and 8500.
    Each node in the tree will have a value between 0 and 25.

Idea:
    1. enumerate all path and reverse it, linear find minimum
    2. dynamically update the max, save space
"""

from typing import List
from helper import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def num2str(num):
            return chr(ord('a')+num)

        def isLeaf(tree):
            return not(tree.left or tree.right)
        
        paths = []
        def dfs(tree,path):
            if tree is None:
                return None
            path.append(tree.val)
            # path+=num2str(tree.val)
            if isLeaf(tree):
                paths.append(path[:])
            
            dfs(tree.left,path)
            dfs(tree.right,path)
            path.pop()
        
        dfs(root,[])
        paths = [x[::-1] for x in paths]
        paths.sort()

        return "".join(num2str(x) for x in paths[0])

    def smallestFromLeaf2(self, root: TreeNode) -> str:
        def cmp(a,b):
            for i in range(min(len(a),len(b))):
                if a[i]>b[i]:
                    return 1
                elif a[i]<b[i]:
                    return -1
                else:
                    pass
            if len(a)>len(b):
                return 1
            elif len(a) < len(b):
                return -1
            else:
                return 0

        def num2str(num):
            return chr(ord('a')+num)

        def isLeaf(tree):
            return not(tree.left or tree.right)
        
        self.best = [26] # gauranteed larger than any number
        def dfs(tree,path):
            if tree is None:
                return None
            path.append(tree.val)
            if isLeaf(tree):
                self.best = min(path[::-1],self.best)
                # self.best = path[::-1] if cmp(path[::-1],self.best) == -1 else self.best
            dfs(tree.left,path)
            dfs(tree.right,path)
            path.pop()
        
        dfs(root,[])

        return "".join(num2str(x) for x in self.best)

if __name__ == '__main__':
    sl = Solution()
    tree = stringToTreeNode("[25,1,3,1,3,0,2]")
    tmp = sl.smallestFromLeaf2(tree)
    print(tmp)