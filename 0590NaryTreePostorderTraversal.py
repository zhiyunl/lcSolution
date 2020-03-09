"""
Given an n-ary tree, return the postorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Follow up:
Recursive solution is trivial, could you do it iteratively?
Idea: iteratively
    1. use stack to record the visited but not output node.
        save root in stack
        for every element in stack, if its a node, save val in stack and push children in reverse order.
        else if its a int, output to res
        until stack is empty
    2. semi pre-order first, reverse in the end
corner:
    1. empty, return []
"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root is None:
            return res
        stack = [root]
        while stack:
            tmp = stack.pop()
            child = tmp.children
            if child:
                tmp.children = []
                stack += [tmp] + child[::-1]
            else:
                res += [tmp.val]
        return res

    def postorder2(self, root: 'Node') -> List[int]:
        res = []
        if root is None:
            return res
        stack = [root]
        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            stack += tmp.children
        return reversed(res)
