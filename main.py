# from countAndSay import Solution
# import time
# start = time.time()
#
# sl = Solution()
# # s = "MCMXCIV"
# # result = sl.romanToInt(s=s)
#
# print(sl.countAndSay(12))
# print("time is %.5f"%((time.time()-start)*10000))

# from defangIPaddr import Solution
# import time
#
# N = 20
# start = time.time()
# for i in range(N):
#     sl = Solution()
#     # str = "192.168.1.1"
#     str = "0.0.0.1"
#     sl.defangIPaddr(str)
#
# print("time is %.5f"%((time.time()-start)*10000/N))
# print(sl.defangIPaddr(str))


# from longestCommonPrefix import Solution
# import time
#
# N = 20
# start = time.time()
# sl = Solution()
# list = ["flower", "flow", "flight"]
# list=["dog","racecar","car"]
# for i in range(N):
#     sl.longestCommonPrefix(list)
#
# print("time is %.5f"%((time.time()-start)*10000/N))
# print(sl.longestCommonPrefix(list))

# import time
# from mergeTwoLists import *
# N = 1
# start = time.time()
# sl = Solution()
# l1 = ListNode(0)
# l2 = ListNode(1)
# sp1 = l1
# sp2 = l2
# for i in range(1, 10):
#     sp1.next = ListNode(i)
#     sp2.next = ListNode(i + 1)
#     sp1 = sp1.next
#     sp2 = sp2.next
# l1 = ListNode(None)
# l2 = ListNode(None)
# # for i in range(N):
# #     sl.mergeTwoLists(l1, l2)
# print("time is %.5f" % ((time.time() - start) * 10000 / N))
# # print(sl.mergeTwoLists(list))
# l = sl.mergeTwoLists(l1, l2)
# while l.next is not None:
#     print(l.val)
#     l = l.next
# print(l.val)

import time
from countAndSay import *

N = 20
n = 30
start = time.time()
sl = Solution()
for i in range(N):
    sl.countAndSay(n)
print("time is %.5f" % ((time.time() - start) * 10000 / N))
print(sl.countAndSay(n))
