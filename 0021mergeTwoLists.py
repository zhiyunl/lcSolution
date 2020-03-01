# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Merge two sorted linked lists and return it as a new list.
New list should be splicing together the nodes of the first two lists
1-2-4 1-3-4 => 1-1-2-3-4-4,
1. easy way to do is check the first element in each list and choose the smallest one
2. since inputs are linked lists, so access will be sequential.
extreme condition: inputs are None or empty lists, return None or Empty
        one is empty and the other is not, just return the other
        in case of a tie, choose l2
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l1.val is None:
            return l2
        if l2 is None or l2.val is None:
            return l1
        l = ListNode(None)
        sp = l
        while True:
            if l1.val < l2.val:
                sp.next = l1
                l1 = l1.next
            else:
                sp.next = l2
                l2 = l2.next
            sp = sp.next
            if l1 is None:
                sp.next = l2
                return l.next
            elif l2 is None:
                sp.next = l1
                return l.next
        return l.next


import time

N = 1
start = time.time()
sl = Solution()
l1 = ListNode(0)
l2 = ListNode(1)
sp1 = l1
sp2 = l2
for i in range(1, 10):
    sp1.next = ListNode(i)
    sp2.next = ListNode(i + 1)
    sp1 = sp1.next
    sp2 = sp2.next
print("time is %.5f" % ((time.time() - start) * 10000 / N))
ll = sl.mergeTwoLists(l1, l2)
while ll.next:
    print(ll.val)
    ll = ll.next
print(ll.val)

# faster than 88%, but more space needed
