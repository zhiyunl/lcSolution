"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

idea:
    1. use stack to pop
    2. change pointer iteratively
    3. recursively find next until NULL, return back up
extreme case:
    recursive method, when
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        # stack
        stack = []
        p = head
        while p:
            stack.append(p.val)
            p = p.next
        head = ListNode(0)
        p = head
        while stack:
            p.next = ListNode(stack.pop())
            p = p.next
        return head.next

    def reverseList2(self, head: ListNode) -> ListNode:
        # iteratively
        p = head
        if not p or not p.next:
            return p
        q = p.next
        r = q.next
        p.next = None
        while q:
            q.next = p
            p = q
            q = r
            r = None if r is None else r.next
        return p

    def reverseList3(self, head: ListNode) -> ListNode:
        # recursively
        def reverse(node: ListNode):
            if not node:
                node = ListNode(0)
                return node, node
            p, tail = reverse(node.next)
            tail.next = node  # trick is here,
            node.next = None
            return p, tail.next

        p, tail = reverse(head)
        return p.next
    # could be simpler, using reverseList3 to replace reverse
