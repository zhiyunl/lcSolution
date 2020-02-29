"""
Given a Binary Search Tree and a target number, return true
if there exist two elements in the BST such that their sum
is equal to the given target.

Input:
    5
   / \
  3   6
 / \   \
2   4   7
Target = 9 Output: True

Input:
    5
   / \
  3   6
 / \   \
2   4   7
Target = 28 Output: False

Idea:
    1. Since the input is BST, similar to sorted array, when we use binary search. nlogn
    2. transfer tree to hash table
    either case, binary search and traversal needs to be done. logn
corner case:
    1. empty tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def preorder(self, tree, target):
        if tree is None:
            return False
        if self.searchBST(self.root, tree, target):
            return True
        if self.preorder(tree.left, target) or self.preorder(tree.right, target):
            return True
        return False

    def searchBST(self, root, node, target):
        if root is None:
            return False
        else:
            if root.val == target - node.val:  # assume no duplicates
                return not (root is node)
            else:
                return self.searchBST(root.left if root.val > target - node.val else root.right, node, target)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.root = root
        return self.preorder(root, k)

    def stringToTreeNode(self, input):
        input = input.strip()
        input = input[1:-1]
        if not input:
            return None

        inputValues = [s.strip() for s in input.split(',')]
        root = TreeNode(int(inputValues[0]))
        nodeQueue = [root]
        front = 0
        index = 1
        while index < len(inputValues):
            node = nodeQueue[front]
            front = front + 1

            item = inputValues[index]
            index = index + 1
            if item != "null":
                leftNumber = int(item)
                node.left = TreeNode(leftNumber)
                nodeQueue.append(node.left)

            if index >= len(inputValues):
                break

            item = inputValues[index]
            index = index + 1
            if item != "null":
                rightNumber = int(item)
                node.right = TreeNode(rightNumber)
                nodeQueue.append(node.right)
        return root


if __name__ == '__main__':
    sl = Solution()
    nums = "[5, 3, 6, 2, 4, null, 7]"
    target = 4
    root = sl.stringToTreeNode(nums)
    tmp = sl.findTarget(root, target)
    print(tmp)
