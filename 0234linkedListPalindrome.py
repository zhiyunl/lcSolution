"""
Given a singly linked list, determine if it's a palindrome
Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up: Could you do it in O(n) time and O(1) space?
idea: using fast and slow pointer to find middle of linked list
    reverse first half, 1.use stack 2.recursive 3.change pointer
     choose third way to achieve using O(1) space
     use three pointer p q r
extreme case:
        [] return True
        [1] return True
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # use stack to reverse
    def isPalindrome1(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        lp = head
        fp = head.next
        stack = []
        while fp is not None and fp.next is not None:
            fp = fp.next.next
            stack.append(lp.val)
            lp = lp.next
        if fp is not None:
            # even
            stack.append(lp.val)
        lp = lp.next  # compare start with next element
        # compare left half with right
        while stack:
            if lp.val != stack.pop():
                return False
            else:
                lp = lp.next
        return True

    def isPalindrome2(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev


import time

start = time.time()
sl = Solution()
l1 = ListNode(0)
sp1 = l1
for i in [2, 1, 2, 1, 3, 1, 2, 1, 2]:
    sp1.next = ListNode(i)
    sp1 = sp1.next
l1 = l1.next
print("time is %.5f" % ((time.time() - start) * 10000))
# bo = sl.isPalindrome1(l1)
bo = sl.isPalindrome2(l1)
print(bo)
