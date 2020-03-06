"""
You are given two non-empty linked lists representing two non-negative
Integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, expect the
number 0 itself.
e.g.: Input (2->4->3) + (5->6->4) Output: 7-> 0-> 7
Idea:
    1. get the len of each number, O(n)
    2. add corresponding digits from head(reversed order), set as sum mod 10, +1 if needed
Corner case:
    1. head=0 and head.next is None: return the other number
    2. empty list: return the other one.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from helper import *


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1

        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        res = 0
        while l1.next is not None and l2.next is not None:
            sum = l1.val + l2.val + res
            l1.val = sum % 10
            res = sum // 10
            l1 = l1.next
            l2 = l2.next

        # remains 1 node and 1 list
        sum = l1.val + l2.val + res
        l1.val = sum % 10
        res = sum // 10
        l1_pre = l1
        l1.next = l2.next if l1.next is None else l1.next
        l1 = l1.next
        # l2 = l2.next
        while l1 is not None:
            sum = l1.val + res
            l1.val = sum % 10
            res = sum // 10
            l1_pre = l1
            l1 = l1.next
        if res == 1:
            l1_pre.next = ListNode(1)
        return head
