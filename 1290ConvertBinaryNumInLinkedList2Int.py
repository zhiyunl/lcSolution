"""
Given head which is a reference node to a singly-linked list.
The value of each node in the linked list is either 0 or 1.
The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0

Example 3:
Input: head = [1]
Output: 1

Example 4:
Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880

Example 5:
Input: head = [0,0]
Output: 0

Constraints:
    The Linked List is not empty.
    Number of nodes will not exceed 30.
    Each node's value is either 0 or 1.
Idea:
    1. use x2 for each node,
    2. bit operation << for binary number
corner:
    1. 0 return 0
"""
from helper import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # bit operation
        cnt = 0
        while head is not None:
            cnt = (cnt << 1) + head.val
            head = head.next
        return cnt


if __name__ == '__main__':
    sl = Solution()
    nums = [1, 0, 1]
    head = list2ListNode(nums)
    tmp = sl.getDecimalValue(head)
    print(tmp)
